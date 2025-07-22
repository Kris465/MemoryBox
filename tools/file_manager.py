import json
from loguru import logger


def read_from_json(title: str):
    with open(title, "r", encoding='UTF-8') as file:
        result_dict = json.load(file)
        return result_dict


def write_to_json(data: dict, file_name: str):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def update_novels_file(novel_name: str, link: str):
    data = read_from_json("novels.json")
    data[novel_name] = link
    write_to_json(data, "novels.json")
    logger.info(link)
