'''
It writes to json
'''

import json

def write(data, name):
    '''
    This method writes a dictionary with links from one page to json file
    '''
    with open(f"projects/{name}.json", "w", encoding="UTF-8") as file:
        json.dump(data, file)
