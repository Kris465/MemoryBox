import json

def write(data):

    with open('notes.txt', 'w') as outfile:
        json.dump(data, outfile)
