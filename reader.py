import json

def read():

    with open('notes.json', 'r') as json_file:
        data = json.load(json_file)
        return data
