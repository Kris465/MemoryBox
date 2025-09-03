import json
import pandas as pd
from datetime import datetime
import argparse


def json_to_excel(json_file_path, excel_file_path=None):
    """
    Конвертирует JSON файл с данными из Yonote в Excel таблицу

    Args:
        json_file_path (str): Путь к JSON файлу
        excel_file_path (str): Путь для сохранения Excel файла (опционально)
    """

    # Читаем данные из JSON
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"Успешно прочитано {len(data)} строк из {json_file_path}")
    except FileNotFoundError:
        print(f"Ошибка: Файл {json_file_path} не найден")
        return
    except json.JSONDecodeError:
        print(f"Ошибка: Файл {json_file_path} содержит некорректный JSON")
        return

    # Если путь для Excel не указан, генерируем автоматически
    if excel_file_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        excel_file_path = f"yonote_data_{timestamp}.xlsx"

    # Подготавливаем данные для DataFrame
    excel_data = []

    for item in data:
        # Создаем словарь для строки Excel
        row_data = {}

        # Добавляем служебные поля
        row_data['row_number'] = item.get('row_number', '')
        row_data['row_index'] = item.get('row_index', '')

        # Добавляем основные колонки
        columns = item.get('columns', {})
        row_data['id'] = columns.get('id', '')
        row_data['name'] = columns.get('name', '')
        row_data['message'] = columns.get('message', '')
        row_data['property_1'] = columns.get('property_1', '')
        row_data['city_region'] = columns.get('city_region', '')
        row_data['contact'] = columns.get('contact', '')
        row_data['occupation'] = columns.get('occupation', '')
        row_data['comment'] = columns.get('comment', '')
        row_data['portfolio_instagram'] = columns.get('portfolio_instagram', '')

        # Добавляем дополнительные колонки (если есть)
        for key, value in columns.items():
            if key.startswith('column_'):
                row_data[key] = value

        excel_data.append(row_data)

    # Создаем DataFrame
    df = pd.DataFrame(excel_data)

    # Сохраняем в Excel
    try:
        df.to_excel(excel_file_path, index=False, engine='openpyxl')
        print(f"Данные успешно сохранены в: {excel_file_path}")
        print(f"Всего строк: {len(df)}")
        print(f"Колонки: {list(df.columns)}")

    except Exception as e:
        print(f"Ошибка при сохранении в Excel: {e}")
        return

    return df


def main():
    """Основная функция для запуска из командной строки"""
    parser = argparse.ArgumentParser(description='Конвертирует JSON из Yonote в Excel')
    parser.add_argument('--json', '-j', default='yonote_data.json',
                        help='Путь к JSON файлу (по умолчанию: yonote_data.json)')
    parser.add_argument('--excel', '-e',
                        help='Путь для сохранения Excel файла (по умолчанию: yonote_data_YYYYMMDD_HHMMSS.xlsx)')
    args = parser.parse_args()
    print("Конвертация JSON в Excel...")
    print(f"Входной файл: {args.json}")

    df = json_to_excel(args.json, args.excel)

    if df is not None:
        print("Конвертация завершена успешно!")
    else:
        print("Конвертация не удалась")


if __name__ == "__main__":
    main()
