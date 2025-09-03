# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint

def lists_func():
    num = int(input("Input the length of the wished list: "))
    ls = [randint(0, 99) for i in range(num)]
    print(ls)
    print([ls[i + 1] for i in range(num - 1) if ls[i] < ls[i + 1]])

lists_func()
