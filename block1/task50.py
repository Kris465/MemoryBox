import math


def distance(point1, point2):
    return math.sqrt(
        (point2[0] - point1[0] ** 2 + (point2[1] - point1[1]) ** 2))


def perimeter(a, b, c):
    return distance(a, b) + distance(b, c) + distance(c, a)


def area(a, b, c):
    ab = distance(a, b)
    bc = distance(b, c)
    ca = distance(c, a)
    s = (ab + bc + ca) / 2
    return math.sqrt(s * (s - ab) * (s - bc) * (s - ca))


x1, y1 = map(float, input("Введите координаты первой вершины(x1, y1): \
").split())
x2, y2 = map(float, input("Введите координаты второй вершины (x2, y2): \
").split())
x3, y3 = map(float, input("Введите координаты второй вершины (x3, y3): \
").split())


A = (x1, y2)
B = (x2, y2)
C = (x3, y3)


tr_perimeter = perimeter(A, B, C)
tr_area = area(A, B, C)


print(f"Периметр треугольника: {tr_perimeter:.2f}")
print(f"Площадь треугольника: {tr_area:.2f}")
