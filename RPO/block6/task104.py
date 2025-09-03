def cut_squares(a, b):
    squares = []
    while a != 0 and b != 0:
        if a > b:
            count = a // b
            squares.append((b, count))
            a = a % b
        else:
            count = b // a
            squares.append((a, count))
            b = b % a
    return squares


a = 425
b = 131
squares = cut_squares(a, b)
print("Исходный прямоугольник будет разрезан на следующие квадраты:")
for size, count in squares:
    print(f"{count} квадратов со стороной {size}")
