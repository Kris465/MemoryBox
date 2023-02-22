# 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

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
        else: print("I'm running...") # Сюда можно вставить continue, но так прикольнее. 
    print("Magic!")

    print(f"Minimum value is: {int(min_frac)}, maximum value is: {int(max_frac)}")
    print(f"Difference between values is: {int(max_frac - min_frac)}")
    
    
creating_a_new_list()
