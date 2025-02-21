from math import sqrt

a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))
P = a + b + a + b
D = sqrt(a*a + b*b)
print(f"Периметр прямоугольника: {P}")
print(f"Диагональ прямоугольника: {D}")
