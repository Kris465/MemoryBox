# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# Workshop3_homework/task1.py

import random

def sum_up_odd_numbers():
    size = int(input("Input the size of the list: "))
    lst = [random.randint(0, 10) for i in range(size)]
    print(*lst)
    sum_up = 0

    print("Your list is:", *[sum_up + lst[i] for i in range(len(lst)) if i % 2 == 0])

sum_up_odd_numbers()