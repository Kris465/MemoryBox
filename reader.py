import json
from datetime import datetime

def read():

    with open('notes.json', 'r') as json_file:
        data = json.load(json_file)
        lst = data.get("id")

        for elem in lst:
            elem['time'] = datetime.strptime(elem.get("time"), "%d/%m/%y %H:%M")

        data = {"id": lst}
        return data
