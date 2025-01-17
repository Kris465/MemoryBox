from math import sin
x = float(input("Введите число: "))
if 0.2 < x < 0.9:
    F = sin(x)
    print(f"F = {F}")
else:
    print("F = 1")
