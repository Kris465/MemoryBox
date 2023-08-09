# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# https://www.geeksforgeeks.org/python-string-ascii_lowercase/


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


create_files("txt", 2, 10, 256, 4096, 4)
