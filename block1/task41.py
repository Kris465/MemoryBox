from math import sin, cos, radians

e = int(input("Введите e: "))
f = int(input("Введите f: "))
g = int(input("Введите g: "))
h = int(input("Введите h: "))
a = round(((((abs(e - (3 / f))) ** 3) + g) ** 0.5), 2)
b = round(sin(radians(e)) + cos(radians(h)) ** 2, 2)
c = round((33 * g) / ((e * f) - 3), 2)
print("a =", a)
print("b =", b)
print("c =", c)
