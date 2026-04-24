import math

x1, y1 = map(float, input("Введите координаты первой вершины (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты второй вершины (x2 y2): ").split())
x3, y3 = map(float, input("Введите координаты третьей вершины (x3 y3): ").split())

AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
CA = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

perimeter = AB + BC + CA
s = perimeter / 2
area = math.sqrt(s * (s - AB) * (s - BC) * (s - CA))

print("Периметр:", perimeter)
print("Площадь:", area)