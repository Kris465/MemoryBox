# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random


def fill_file(filename, num_lines):
    with open(filename, 'a') as f:
        for i in range(num_lines):
            int_num = random.randint(-1000, 1000)
            float_num = round(random.uniform(-1000, 1000), 2)
            f.write(str(int_num) + '|' + str(float_num) + '\n')


fill_file("task1.txt", 10)
