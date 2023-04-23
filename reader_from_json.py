import json

def read(title):
    with open(f'{title}.json', encoding="UTF-8") as file:
        file = json.load(file)
        return file
