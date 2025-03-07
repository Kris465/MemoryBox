def print_numbers_with_square_not_exceeding_n(n):
    i = 1
    while True:
        square = i * i
        if square > n:
            break
        print(i, end=" ")
        i += 1
    print()


def find_first_number_with_square_greater_than_n(n):
    i = 1
    while True:
        square = i * i
        if square > n:
            return i
        i += 1


n = int(input("Введите число n: "))

# Решение части (а)
print("Натуральные числа, квадрат которых не превышает", n, ":")
print_numbers_with_square_not_exceeding_n(n)

# Решение части (б)
result = find_first_number_with_square_greater_than_n(n)
print("Первое натуральное число, квадрат которого больше", n, ":", result)
