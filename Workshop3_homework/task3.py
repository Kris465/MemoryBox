# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def creating_a_new_list():
    size = int(input("Input the size of the list: "))
    lst = []

    for i in range(size):
        lst.append(round(random.randint(0, 10) + random.random(), 1))
    
    print(f"Random list is: {lst}")

    max_frac = 0
    min_frac = 9

    for i in range(len(lst)):
        if (lst[i] * 10) % 10 > max_frac:
            max_frac = (lst[i] * 10) % 10
        elif (lst[i] * 10) % 10 < min_frac:
            min_frac = (lst[i] * 10) % 10
        else: print("I'm running!")

    print(f"Minimum value is: {int(min_frac)}, maximum value is: {int(max_frac)}")
    print(f"Difference between values is: {int(max_frac - min_frac)}")
    
    
creating_a_new_list()