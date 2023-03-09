import json

def write(data):

    lst = data.get("id")

    for elem in lst:
        elem['time'] = elem.get("time").strftime("%d/%m/%y %H:%M")

    data = {"id": lst}
    
    with open('notes.json', 'w') as outfile:
        json.dump(data, outfile)
