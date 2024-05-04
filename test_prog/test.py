import json
with open('main.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(data)
keys=list(data.keys())
print(keys)
second_key=keys[-1]
print(second_key)
