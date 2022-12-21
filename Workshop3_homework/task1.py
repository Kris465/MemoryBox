# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

from random import randint

def creating_a_new_list():
    size = int(input("Input the size of the list: "))
    lst = []

    for i in range(size):
        lst.append(randint(0, 10))
    
    print(f"Random list is: {lst}")
    return lst

def sum_up_odd_numbers(random_list):

    sum_up = 0

    for pos in range(len(random_list)):
        if pos % 2 == 0:
            sum_up += random_list[pos]
        else: sum_up += 0
        print(pos + 1, random_list[pos], end = "\n")
    
    print(f"Asked sum is: {sum_up}")

my_list = creating_a_new_list()
sum_up_odd_numbers(my_list)
