import math


def length_of_segment(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def perimeter_of_triangle(x1, y1, x2, y2, x3, y3):
    side_a = length_of_segment(x1, y1, x2, y2)
    side_b = length_of_segment(x2, y2, x3, y3)
    side_c = length_of_segment(x3, y3, x1, y1)
    return side_a + side_b + side_c


x1, y1 = 0, 0
x2, y2 = 3, 0
x3, y3 = 0, 4

perimeter = perimeter_of_triangle(x1, y1, x2, y2, x3, y3)
print(f"Периметр треугольника: {perimeter}")
