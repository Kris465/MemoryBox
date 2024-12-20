def find_n(x):
    last_digit = x % 10
    result = (x - last_digit) // 10
    n = last_digit * 100 + result
    return n


def find_x(n):
    last_digit = n // 100
    result = n % 100
    x = result * 10 + last_digit
    return x


x = int(input("Введите число: "))
n = find_n(x)
print(n)

n_input = int(input("Введите n: "))
x_result = find_x(n_input)
print(x_result)
