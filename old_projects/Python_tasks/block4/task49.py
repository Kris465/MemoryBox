import math

a = int(input("Введите число а = "))
b = int(input("Введите число b = "))
c = int(input("Введите число c = "))

if a == 0:
    print("Ошибка а не должен быть равен 0")

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(F"Уравнение имеет два различных корня: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2 * a)
    print(f"Уравнение имеет один корень: x = {x}")
else:
    print("Уравнение не имеет вещественных корней")
