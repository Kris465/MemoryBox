# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

def creating_a_new_list():
    size = int(input("Input the size of the list: "))
    lst = []

    for i in range(size):
        lst.append(randint(0, 10))
    
    print(f"Random list is: {lst}")
    return lst

def unique_numbers(some_list):
    lst_doubles = {}
    lst_unique = []

    for i in some_list: 
        if i not in lst_unique: 
            lst_unique.append(i) 

    print(f"Unique numbers are: {lst_unique}")


    for e in some_list:
        lst_doubles[e] = lst_doubles.get(e, 0) + 1

        doubles = {e: count for e, count in lst_doubles.items() if count > 1}

    print(f"Double numbers are: {doubles}")

            
random_list = creating_a_new_list()
unique_numbers(random_list)