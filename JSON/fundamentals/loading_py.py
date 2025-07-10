import json
# Basic JSON Decoding


loader = json.load(fp=str)


with open('loading.json','r') as f:
    result = loader(f)
print(result)