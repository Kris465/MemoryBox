from math import sqrt
x1 = float(input("Введите число x1: "))
y1 = float(input("Введите число y1: "))
x2 = float(input("Введите число x1: "))
y2 = float(input("Введите число y2: "))


def distance(x1, y1, x2, y2):
    c = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return c


c = distance(x1, y1, x2, y2)
print(c)
