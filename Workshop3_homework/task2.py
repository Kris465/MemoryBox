# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

def creating_a_new_list():
    size = int(input("Input the size of the list: "))
    lst = []

    for i in range(size):
        lst.append(randint(0, 10))
    
    print(lst)
    
    multi_list = []
    k = 0

    if size % 2 == 0:
        new_size = size
    else: new_size = size + 2

    for i in range(new_size // 2):
        multi_list.append(lst[k] * lst[ - (k + 1)])
        k += 1
        
    print(multi_list)


creating_a_new_list()