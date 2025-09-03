import json
import re
from pathlib import Path


def clean_text(text):
    text = text.replace('â', '"').replace('â', '"')
    text = text.replace('â¦', '...')  # Многоточие
    text = text.replace('â', "'").replace('â', "'")

    text = re.sub(r'[^\x20-\x7E\u0400-\u04FF\n\r\t]', '', text)
    text = '\n'.join(line.strip() for line in text.split('\n'))

    return text


def clean_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Ошибка чтения JSON: {e}")
            return False

    cleaned_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            cleaned_data[key] = clean_text(value)
        else:
            cleaned_data[key] = value

    backup_path = file_path.with_suffix('.json.bak')
    try:
        Path(file_path).rename(backup_path)
    except Exception as e:
        print(f"Не удалось создать резервную копию: {e}")
        return False

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

    return True


if __name__ == "__main__":
    file_path = Path(input("Введите путь к JSON файлу: ").strip())

    if file_path.exists() and file_path.suffix.lower() == '.json':
        if clean_json_file(file_path):
            print("Файл успешно очищен и сохранен!")
            print(f"Оригинальный файл сохранен как: {file_path.with_suffix('.json.bak')}")
        else:
            print("Не удалось обработать файл.")
    else:
        print("Указанный файл не существует или не является JSON файлом.")
