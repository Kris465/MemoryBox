from math import sin, radians
d1 = int(input("Введите основание d1:"))
d2 = int(input("Введите угол: "))
a = int(input("Введите угол: "))
s = round(0.5 * d1 * d2 * sin(radians(a)), 2)
print("Площадь =", s)
