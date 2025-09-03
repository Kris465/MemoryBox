# Задача 5 VERY HARD SORT необязательная

# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint

def sorted_array():
    row = int(input("Input number: "))
    column = int(input("Input number: "))
    a = [[randint(1, 10) for j in range(column)] for i in range(row)]
    print(a)






sorted_array()
