import json


def read(title):
    with open(f'{title}.json', encoding="UTF-8") as file:
        file = json.load(file)
        return file


def read_chi(title):
    with open('file.json', 'r', encoding='gbk') as f:
        data = json.load(f)
        return data
