from math import radians, sin, cos
v0 = int(input("Введите начальную скорость: "))
a = int(input("Введите угол падения: "))
t = int(input("Введите время: "))
p = int(input("Введите высоту цели: "))
h = int(input("Введите высоту на которой находится предмет: "))
r = int(input("Введите расстояние от пушки до цели: "))
g = 9.8
x = v0 * t * cos(radians(a))
y = v0 * t * sin(radians(a)) * ((g * (t ** 2)) / 2)
if x == r and y > h and y < p:
    print("Да, попадёт снаряд")
else:
    print("Нет, не попадёт снаряд")
