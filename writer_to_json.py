import json


def write(name, data):
    with open(f"{name}.json", "w", encoding="UTF-8") as file:
        json.dump(data, file)
