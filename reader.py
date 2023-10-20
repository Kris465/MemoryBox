import json
import docx
import os


def read(title):
    full_name = find_file(title)
    _, ext = os.path.splitext(full_name)
    if ext == '.json':
        with open(f'{title}', encoding="UTF-8") as file:
            data = json.load(file)
    elif ext == '.txt':
        with open(f'{title}', encoding="UTF-8") as file:
            data = file.read()
    elif ext == '.docx':
        doc = docx.Document(f'{title}')
        data = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    else:
        raise ValueError('Unsupported format')

    return data


def find_file(name):
    for file in os.listdir('.'):
        if file.startswith(name):
            return file
    raise ValueError('File not found')
