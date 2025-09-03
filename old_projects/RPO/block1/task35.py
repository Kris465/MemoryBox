from math import sqrt


a = float(input("Введите положительное число a: "))
b = float(input("Введите положительное число b: "))

if a <= 0 or b <= 0:
    print(None)
else:

    c = sqrt(a ** 2 + b ** 2)

    rounded_c = round(c, 2)
    print(rounded_c)
