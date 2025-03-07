def find_first_square_greater_than_n(n):
    i = 1
    while True:
        square = i * i
        if square > n:
            return square
        i += 1


n = int(input("Введите число n: "))
result = find_first_square_greater_than_n(n)
print(f"Первое число, большее {n}, в последовательности квадратов: {result}")
