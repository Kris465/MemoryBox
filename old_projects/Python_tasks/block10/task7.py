import math

a1 = float(input("Введите длину меньшего основания первой трапеции (a1): "))
b1 = float(input("Введите длину большего основания первой трапеции (b1): "))
h1 = float(input("Введите высоту первой трапеции (h1): "))


a2 = float(input("Введите длину меньшего основания второй трапеции (a2): "))
b2 = float(input("Введите длину большего основания второй трапеции (b2): "))
h2 = float(input("Введите высоту второй трапеции (h2): "))


def calculate_trapezoid_perimeter(a, b, h):
    c = math.sqrt(h**2 + ((b - a) / 2)**2)
    perimeter = a + b + 2 * c
    return perimeter


perimeter1 = calculate_trapezoid_perimeter(a1, b1, h1)
perimeter2 = calculate_trapezoid_perimeter(a2, b2, h2)

total_perimeter = perimeter1 + perimeter2

print(f"Сумма периметров двух равнобедренных трапеций: {
    round(total_perimeter, 2)}")
