# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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

    for index in range(len(random_list)):
        if index % 2 != 0:
            sum_up += random_list[index]
        else: sum_up += 0
        print(index, random_list[index], end = "\n")
    
    print(f"Asked sum is: {sum_up}")

my_list = creating_a_new_list()
sum_up_odd_numbers(my_list)