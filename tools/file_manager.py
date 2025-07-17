import json


def read_from_json(title: str):
    with open(title, "r", encoding='UTF-8') as file:
        result_dict = json.load(file)
        return result_dict


def write_to_json():
    pass
