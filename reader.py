import json

def read(name):
    with open(f'{name}.json', 'r', encoding=None) as json_file:
        data = json.load(json_file)
        lst = data.get(name)
        return lst
