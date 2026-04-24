import math


def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)


x1 = float(input("Введите координату x первой вершины (x1): "))
y1 = float(input("Введите координату y первой вершины (y1): "))
x2 = float(input("Введите координату x второй вершины (x2): "))
y2 = float(input("Введите координату y второй вершины (y2): "))
x3 = float(input("Введите координату x третьей вершины (x3): "))
y3 = float(input("Введите координату y третьей вершины (y3): "))
x4 = float(input("Введите координату x четвёртой вершины (x4): "))
y4 = float(input("Введите координату y четвёртой вершины (y4): "))

# Вычисление площади двух треугольников, образованных четырьмя вершинами
area1 = triangle_area(x1, y1, x2, y2, x3, y3)
area2 = triangle_area(x1, y1, x3, y3, x4, y4)

total_area = area1 + area2

print("Площадь четырехугольника:", total_area)
