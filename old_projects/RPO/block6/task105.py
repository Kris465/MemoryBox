def cut_squares(a, b):
    squares = []
    while a > 0 and b > 0:
        if a < b:
            size = a
            count = b // a
            b -= size * count
        else:
            size = b
            count = a // b
            a -= size * count

        squares.append((size, count))
    return squares


a = 6
b = 4
result = cut_squares(a, b)
print("Размеры квадратов и их количество:", result)
