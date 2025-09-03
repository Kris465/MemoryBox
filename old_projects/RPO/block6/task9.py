import math

n = int(int(input("Введите число: ")))

def find_first_square_greater_than_n(n):
    i = 1
    while i * i <= n:
        i += 1
    return i * i


result = find_first_square_greater_than_n(n)
print("Первое число больше", n, "равно:", result)
