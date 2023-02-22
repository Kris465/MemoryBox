# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

def mix_list():
    size = int(input("Input the size of your list: "))
    lst = []
    imin = int(input("Input the minimum number: "))
    imax = int(input("Input the maximum number: "))
  
    for i in range(size):
        lst.append(random.randint(imin, imax))
    print(lst)

    for i in range(len(lst)):
        rnd = random.randint(0, len(lst) - 1)
        temp = lst[i]
        lst[i] = lst[rnd]
        lst[rnd] = lst[i]    
    print(lst)

mix_list()
