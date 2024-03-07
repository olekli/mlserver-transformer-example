import requests

inference_request = {
  'inputs': [
    {
      'name': 'args',
      'shape': [ 1 ],
      'datatype': 'BYTES',
      'data': [ 'Once upon a time there was...' ],
    },
  ],
  'parameters': {
    'extra': { 'max_new_tokens': 2000 }
  }
}

response = requests.post('http://localhost:8080/v2/models/distilgpt2/infer', json = inference_request).json()
print(response)
