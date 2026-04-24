import json


def write(data):
    with open('data.json', 'w', encoding="UTF-8") as f:
        json.dump(data, f)


def read():
    try:
        with open('data.json', 'r+', encoding="UTF-8") as f:
            data = json.load(f)
    except Exception as e:
        data = {"key": "value"}
    return data
