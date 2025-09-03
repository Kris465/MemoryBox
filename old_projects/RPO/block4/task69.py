def rectangles_relationship(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    def is_inside(r1, r2):
        x1, y1, w1, h1 = r1
        x2, y2, w2, h2 = r2
        return (x2 <= x1 and y2 <= y1 and
                x1 + w1 <= x2 + w2 and y1 + h1 <= y2 + h2)

    def is_contained(r1, r2):
        x1, y1, w1, h1 = r1
        x2, y2, w2, h2 = r2
        return (x1 >= x2 and y1 >= y2 and
                x1 + w1 <= x2 + w2 and y1 + h1 <= y2 + h2)

    def is_intersecting(r1, r2):
        x1, y1, w1, h1 = r1
        x2, y2, w2, h2 = r2
        return not (x1 + w1 < x2 or x2 + w2 < x1 or
                    y1 + h1 < y2 or y2 + h2 < y1)

    inside_first_in_second = is_inside(rect1, rect2)
    inside_secoind_in_first = is_inside(rect2, rect1)
    intersecting = is_intersecting(rect1, rect2)

    return inside_first_in_second, inside_secoind_in_first, intersecting


x1 = int(input("Введите первую точку первого прямоугольника: "))
y1 = int(input("Введите вторую точку первого прямоугольника: "))
w1 = int(input("Введите ширину первого прямоугольника: "))
h1 = int(input("Введите высоту первого прямоугольника: "))
rect1 = (x1, y1, w1, h1)
x2 = int(input("Введите первую точку второго прямоугольника: "))
y2 = int(input("Введите вторую точку второго прямоугольника: "))
w2 = int(input("Введите ширину второго прямоугольника: "))
h2 = int(input("Введите высоту второго прямоугольника: "))
rect2 = (x2, y2, w2, h2)

inside_first_in_second, inside_second_in_first, intersecting \
    = rectangles_relationship(rect1, rect2)

print("точки первого прямоугольника принадлежит второму:",
      inside_first_in_second)
print("точки второго прямоугольника принадлежат первому:",
      inside_second_in_first)
print("Прямоугольники пересекаются", intersecting)
