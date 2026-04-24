def triangle_area(x1, x2, y1, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)


def quadrilateral_area(A, B, C, D):
    area1 = triangle_area(A[0], A[1], B[0], B[1], C[0], C[1])
    area2 = triangle_area(A[0], A[1], C[0], C[1], D[0], D[1])
    return area1 + area2


x1, y1 = map(float, input("Введите координаты первой вершины \
    (x1, y1):").split())
x2, y2 = map(float, input("Введите координаты второй вершины \
    (x2, y2):").split())
x3, y3 = map(float, input("Введите координаты третей вершины \
    (x3, y3):").split())
x4, y4 = map(float, input("Введите координаты четвертой вершины \
    (x4, y4):").split())


A = (x1, y1)
B = (x2, y2)
C = (x3, y3)
D = (x4, y4)


quad_area = quadrilateral_area(A, B, C, D)
print(f"Площадь четырехугогльника: {quad_area:.2f}")
