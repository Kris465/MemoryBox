from math import sin
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))


x = round(((2 / (((a ** 2) + 25) + b)) + b) / ((b ** 0.5) + ((a + b) / 2)), 2)
y = round((abs(a) + (2 * sin(b))) / (5.5 * a), 2)
print("x = ", x)
print("y = ", y)
