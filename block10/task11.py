def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2


def polygon_area(x_coords, y_coords):
    n = len(x_coords)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += x_coords[i] * y_coords[j]
        area -= y_coords[i] * x_coords[j]
    return abs(area) / 2


x = []
y = []

for i in range(1, 6):
    xi = float(input(f"Введите x{i}: "))
    yi = float(input(f"Введите y{i}: "))
    x.append(xi)
    y.append(yi)


area = polygon_area(x, y)
print(f"Площадь пятиугольника: {area}")
