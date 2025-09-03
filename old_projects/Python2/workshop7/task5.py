# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

import os
import random
import string


def create_files(extension, min_name_length=6,
                 max_name_length=30, min_bytes=256,
                 max_bytes=4096, num_files=42):
    for _ in range(num_files):
        name_length = random.randint(min_name_length, max_name_length)
        file_name = ''.join(random.choices(string.ascii_lowercase,
                                           k=name_length)) + '.' + extension

        num_bytes = random.randint(min_bytes, max_bytes)
        file_content = os.urandom(num_bytes)

        with open(file_name, 'wb') as f:
            f.write(file_content)


def generate_files(files: dict):
    for k, v in files.items():
        extension = k
        num_files = v
        if num_files > 0:
            create_files(extension=extension, num_files=num_files)


files = {'txt': 10, 'docx': 5, 'pdf': 3}
generate_files(files)
