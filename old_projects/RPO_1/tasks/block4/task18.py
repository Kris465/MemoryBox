def read_rectangle_coords(rect_num):
    """
    Читает координаты прямоугольника по номеру.
    Возвращает кортеж (x1, y1, x2, y2).
    """
    x1 = float(input(f"Координата x левого нижнего угла {rect_num}"))
    y1 = float(input(f"Координата y левого нижнего угла {rect_num}"))
    x2 = float(input(f"Координата x правого нижнего угла {rect_num} "))
    y2 = float(input(f"Координата y правого нижнего угла {rect_num} "))
    return x1, y1, x2, y2


def main():
    rect1 = read_rectangle_coords(1)
    rect2 = read_rectangle_coords(2)

    min_x = min(rect1[0], rect1[2], rect2[0], rect2[2])
    max_x = max(rect1[0], rect1[2], rect2[0], rect2[2])
    min_y = min(rect1[1], rect1[3], rect2[1], rect2[3])
    max_y = max(rect1[1], rect1[3], rect2[1], rect2[3])

    print(f"Левый нижний угол: ({min_x}, {min_y})")
    print(f"Правый верхний угол: ({max_x}, {max_y})")


if __name__ == "__main__":
    main()