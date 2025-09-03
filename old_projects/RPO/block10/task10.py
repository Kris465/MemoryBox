import math


def triangle_area_by_sides(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


a = 3.0
b = 4.0
c = 5.0

area_triangle = triangle_area_by_sides(a, b, c)
print(f"Площадь треугольника: {area_triangle}")
