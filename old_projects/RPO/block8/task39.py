def find_rectangles(s):
    rectangles = []
    for a in range(1, int(s ** 0.5) + 1):
        if s % a == 0:
            b = s // a
            rectangles.append((a, b))
    return rectangles


s = int(input("Введите площадь прямоугольника: "))
rectangles = find_rectangles(s)
print("Размеры всех прямоугольников с площадью", s, ":")
for rectangle in rectangles:
    print(rectangle)
