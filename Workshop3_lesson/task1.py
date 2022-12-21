# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая определит, присутствует ли в заданном списке число,
# полученное от пользователя.

from random import randint

def number_in_list():
    n = int(input("Input your number, please: "))
    lst = []

    for i in range(n):
        lst.append(randint(0, 100))

    print(*lst)

    num = int(input("What should I find? "))
    if num in lst:
        print(f"The number - {num} is present in the list.")
    else: print("There isn't such number.")

number_in_list()
