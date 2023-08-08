# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random

vowels = ['а', 'е', 'ё', 'и', 'о', 'y', 'ы', 'э', 'ю', 'я']


def generate_name():
    length = random.randint(4, 7)
    name = ''
    for i in range(length):
        if i == 0:
            name += random.choice('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
        else:
            name += random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    if not any(v in name for v in vowels):
        return generate_name()
    return name


def fill_file(filename, num_names):
    with open(filename, 'a', encoding="UTF-8") as f:
        for i in range(num_names):
            name = generate_name()
            f.write(name + '\n')


fill_file('task2.txt', 10)
