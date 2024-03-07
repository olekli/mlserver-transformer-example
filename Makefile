dep:
	pip install mlserver mlserver-huggingface	

distilgpt2:
	mkdir -p staging
	cd staging && GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/distilbert/distilgpt2
	cd staging/distilgpt2 && git lfs fetch --include model.safetensors && git lfs checkout model.safetensors
	mkdir distilgpt2
	cd distilgpt2 && ln -sf ../staging/distilgpt2/model.safetensors ../staging/distilgpt2/*.json . && ln -sf ../distilgpt2-model-settings.json model-settings.json

run:
	mlserver start distilgpt2

infer:
	python test.py
