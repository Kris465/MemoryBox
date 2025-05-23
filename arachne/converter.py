import json

# Путь к файлу
input_file = 'novel_content.json'
output_file = 'data_modified.json'

# Функция для рекурсивной обработки строк
def process_strings(data):
    if isinstance(data, dict):
        return {key: process_strings(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [process_strings(item) for item in data]
    elif isinstance(data, str):
        # Добавляем \n перед каждой кавычкой "
        return data.replace('"', '\n"')
    else:
        return data

# Чтение JSON
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Обработка данных — замена " на \n"
modified_data = process_strings(data)

# Запись обратно
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(modified_data, f, ensure_ascii=False, indent=4)

print("Файл успешно обработан и сохранён как", output_file)
