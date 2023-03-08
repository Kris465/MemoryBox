import json

def write(data):

    with open('notes.json', 'w') as outfile:
        json.dump(data, outfile)
