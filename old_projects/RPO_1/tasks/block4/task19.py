def read_rectangle():
    """
    Читает сведения о прямоугольнике: координаты левого нижнего угла и размеры.
    Возвращает кортеж: (x1, y1, width, height)
    """
    x1 = float(input("Введите x левого нижнего угла: "))
    y1 = float(input("Введите y левого нижнего угла: "))
    width = float(input("Введите длину стороны по x (ширина): "))
    height = float(input("Введите длину стороны по y (высота): "))
    return x1, y1, width, height


def main():
    print("Введите параметры первого прямоугольника:")
    rect1 = read_rectangle()

    print("\nВведите параметры второго прямоугольника:")
    rect2 = read_rectangle()

    # Вычисляем правый верхний углы
    x2_1 = rect1[0] + rect1[2]
    y2_1 = rect1[1] + rect1[3]

    x2_2 = rect2[0] + rect2[2]
    y2_2 = rect2[1] + rect2[3]

    # Находим минимальные и максимальные координаты
    min_x = min(rect1[0], rect2[0])
    max_x = max(x2_1, x2_2)

    min_y = min(rect1[1], rect2[1])
    max_y = max(y2_1, y2_2)

    # Выводим результаты
    print(f"\nМинимальный прямоугольник:")
    print(f"Левый нижний угол: ({min_x}, {min_y})")
    print(f"Правый верхний угол: ({max_x}, {max_y})")


if __name__ == "__main__":
    main()
