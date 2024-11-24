from math import sqrt


def my_func(a):
    y = (a * a + 10) / sqrt(a * a + 1)
    return y


a = int(input("Введите значение a: "))
print(my_func(a))
