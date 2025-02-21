from math import pi
r = int(input("Введите радиус: "))
c = round(2 * pi * r, 2)
s = round(pi * (r ** 2), 2)
print("Длина окружности =", c)
print("Площадь круга =", s)
