import math


def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


AB = float(input("Введите длину стороны AB: "))
AD = float(input("Введите длину стороны AD: "))
DC = float(input("Введите длину стороны DC: "))
BC = calculate_hypotenuse(AB, AD)
perimeter = AB + BC + DC + AD
print(f"Периметр фигуры ABCD: {perimeter}")
