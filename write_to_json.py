import json


def write(name, data, language=None):
    with open(f"{name}.json", "w", encoding='UTF-8') as file:
        if language == 'zh':
            json.dump(data, file, ensure_ascii=False)
        else:
            json.dump(data, file)
