def print_squares_not_exceeding_n(n):
    i = 1
    while True:
        square = i * i
        if square > n:
            break
        print(square)
        i += 1


n = int(input("Введите число n: "))
print_squares_not_exceeding_n(n)
