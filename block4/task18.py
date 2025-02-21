def find_minimal_reactangle(x1, y1, x2, y2, x3, y3, x4, y4):
    # Левый нижний угол прямоугольника
    new_x1 = min(x1, x3)
    new_y1 = min(y1, y3)

    # Правый верхний угол прямоугольника
    new_x2 = max(x2, x4)
    new_y2 = max(y2, y4)

    return new_x1, new_y1, new_x2, new_y2


rect1 = (0, 0, 5, 10)
rect2 = (3, 6, 8, 12)

new_rect = find_minimal_reactangle(rect1[0], rect1[1], rect1[2], rect1[3],
                                   rect2[0], rect2[1], rect2[2], rect2[3])

print(f"Левый нижний угол прямоугольника: ({new_rect[0]}, {new_rect[1]})")
print(f"Правый верхний угол прямоугольника: ({new_rect[2]}, {new_rect[3]})")
