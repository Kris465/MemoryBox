import math


def perimeter(a, b, c):
    return a + b + c


def area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


side_a1 = float(input("Введите сторону A1: "))
side_b1 = float(input("Введите сторону B1: "))
side_c1 = float(input("Введите сторону C1: "))

side_a2 = float(input("Введите сторону A2: "))
side_b2 = float(input("Введите сторону B2: "))
side_c2 = float(input("Введите сторону C2: "))

perimeter_1 = perimeter(side_a1, side_b1, side_c1)
area_1 = area(side_a1, side_b1, side_c1)

perimeter_2 = perimeter(side_a2, side_b2, side_c2)
area_2 = area(side_a2, side_b2, side_c2)

total_perimeter = perimeter_1 + perimeter_2
total_area = area_1 + area_2

print(f"Сумма периметров: {total_perimeter:.2f}")
print(f"Сумма площадей: {total_area:.2f}")
