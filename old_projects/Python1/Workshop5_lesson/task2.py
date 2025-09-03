# Создайте список, в который попадают числа. описывающие возрастающую последовательность. Порядок элементов менять нельзя.

from random import choices

def make_list():
    num = int(input("Input the length: "))
    ls = choices(range(num*2), k=num)
    print(ls)
    return ls

def new_lists(lst):
    lst = []
    for i in range(len(lst)):
        temp = lst[i]
        d_list = [temp]
        for j in range(i + 1, len(lst)):
            if lst[j] > temp:
                temp = lst[j]
                d_list.append(temp)
        if len(d_list) > 1:
            lst.append(d_list)
    return  lst


print(new_lists(make_list())) 