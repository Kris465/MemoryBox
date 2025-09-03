# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randint

def creating_a_new_list():
    size = int(input("Input the size of the list: "))
    if size <= 0:
        print("Size can't be less than 0, please, try again!")
    else:
        lst = []

        for i in range(size):
            lst.append(randint(0, 10))
    
        print(f"Random list is: {lst}")
    return lst

def unique_numbers(some_list):
    lst_unique = []

    for i in some_list: 
        if i not in lst_unique: 
            lst_unique.append(i) 

    print(f"Unique numbers are: {lst_unique}")
            
random_list = creating_a_new_list()
unique_numbers(random_list)
