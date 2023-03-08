import json

def read():

    with open('data.txt') as json_file:
        data = json.load(json_file)
        return data
