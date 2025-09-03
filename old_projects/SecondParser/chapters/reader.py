'''
This method reads list from the json file
'''
import json

def read(name):
    '''
    Reader method
    '''
    with open(f'projects/{name}.json', 'r', encoding=None) as json_file:
        data = json.load(json_file)
        lst = data.get(name)
        return lst
