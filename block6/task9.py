import math

def find_first_square_greater_than_n(n):
    i = 1
    while i * i <= n:
        i += 1
    return i * i


n = 20
result = find_first_square_greater_than_n(n)
print("Первое число больше", n, "равно:", result)
