from math import sqrt

a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))

p = a + b + a + b
d = sqrt(a * a + b * b)

print(f"Периметр прямоугольника: {p}")
print(f"Диагональ прямоугольника: {d}")
