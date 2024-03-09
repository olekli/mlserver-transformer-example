import re
import os
import click
from collections import OrderedDict
from huggingface_hub import file_exists, list_repo_tree, hf_hub_download

ModelFileTypes = OrderedDict({
  'safetensors': 'model.safetensors',
  'pytorch': 'pytorch_model.bin',
})

@click.command()
@click.option('--model', required = True, help = 'name of model')
@click.option('--target-dir', required = True, help = 'directory to download to')
def downloadModel(model, target_dir):
  files = list_repo_tree(model)
  files = [ file.path for file in files ]

  to_be_downloaded = []

  for model_file_type in ModelFileTypes:
    if ModelFileTypes[model_file_type] in files:
      to_be_downloaded.append(ModelFileTypes[model_file_type])
      break

  assert to_be_downloaded, 'no model'

  json_file_pattern = re.compile('.*\.json')
  to_be_downloaded += [ file for file in files if json_file_pattern.match(file) ]

  os.makedirs('dest_dir', exist_ok=True)

  for file in to_be_downloaded:
    hf_hub_download(
      repo_id = model,
      filename = file,
      local_dir = target_dir,
      local_dir_use_symlinks = False
    )

if __name__ == '__main__':
  downloadModel()
