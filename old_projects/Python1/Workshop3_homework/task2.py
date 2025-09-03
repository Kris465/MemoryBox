# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import randint

def the_multilist_of_pairs():
    size = int(input("Input the size of the list: "))
    lst = []

    for i in range(size):
        lst.append(randint(0, 10))
    
    print(f"Random list is: {lst}")
    
    multi_list = []

    if size % 2 == 0:
        for i in range(size // 2):
            multi_list.append(lst[i] * lst[-(i + 1)])
    else: 
        for i in range(size // 2):
            multi_list.append(lst[i] * lst[-(i + 1)])
        multi_list.append(lst[i + 1])
        
    print(f"New list which consists of multiplicated pairs is: {multi_list}")


the_multilist_of_pairs()
