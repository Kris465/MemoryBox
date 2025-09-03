from math import sin, radians

x = int(input("Введите число: "))
if x > 0:
    primer_one = sin(radians(x)) ** 2
    print(f"Ответ: {primer_one}")
else:
    primer_two = 1 - 2 * sin(radians(x * x))
    print(f"Ответ: {primer_two}")
