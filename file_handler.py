import json
import logging


def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
        logging.info(f"Данные успешно сохранены в {filename}.")
    except Exception as e:
        logging.error(f"Ошибка при сохранении данных в файл: {e}")


def load_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        logging.info(f"Данные успешно загружены из {filename}.")
        return data
    except Exception as e:
        logging.error(f"Ошибка при загрузке данных из файла: {e}")
        return None
