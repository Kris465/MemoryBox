# Реализуйте алгоритм перемешивания списка.

import random

def random_mixed_list():
    size = int(input("Input the size of your list: "))
    lst = []
    iMin = int(input("Input the minimum number: "))
    iMax = int(input("Input the maximum number: "))
  
    for i in range(size):
        lst.append(random.randint(iMin, iMax))
    print(lst)

    for i in range(len(lst)):
        rnd = random.randint(0, len(lst) - 1)
        temp = lst[i]
        lst[i] = lst[rnd]
        lst[rnd] = lst[i]
    print(lst)
        
random_mixed_list()