def find_n(x):
    last_digit = x % 10  # Последняя цифра числа x
    rest_part = x // 10  # Остальные цифры числа x
    n = last_digit * 10**(len(str(rest_part)) + 1) + rest_part  # Формула для n
    return n


def find_x(n):
    last_digit = n // 10**(len(str(n))-1)
    rest_part = n % 10**(len(str(n))-1)
    x = rest_part * 10 + last_digit
    return x


x = int(input("Введите число x: "))
n = find_n(x)
print(f"Число n: {n}")

n_input = int(input("Введите число n: "))
x_result = find_x(n_input)
print(f"Восстановленное число x: {x_result}")
