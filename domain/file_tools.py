import json
import docx
import os


async def read(title):
    full_name = await find_file(title)
    _, ext = os.path.splitext(full_name)
    if ext == '.json':
        with open(f'{full_name}', encoding="UTF-8") as file:
            data = json.load(file)
    elif ext == '.txt':
        with open(f'{full_name}', encoding="UTF-8") as file:
            data = file.read()
    elif ext == '.docx':
        doc = docx.Document(f'{full_name}')
        data = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    else:
        raise ValueError('Unsupported format')

    return data


async def find_file(name):
    for file in os.listdir('.'):
        if file.startswith(name):
            return file
    raise ValueError('File not found')


async def write_txt(name, data):
    with open(os.path.join(f"{name}.txt"),
              "a", encoding="UTF-8") as file:
        file.write(data)


async def write(name, data, language=None):
    with open(os.path.join(f"{name}.json"),
              "w", encoding='UTF-8') as file:
        json.dump(data, file, ensure_ascii=False)
