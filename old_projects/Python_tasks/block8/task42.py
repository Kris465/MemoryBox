import math


def compute_fraction(m, n):
    numerator = m
    denominator = math.factorial(n)
    fraction = numerator / denominator
    return fraction


m = int(input("Введите натуральное число m: "))
n = int(input("Введите натуральное число n: "))

result = compute_fraction(m, n)
print(f"Результат вычисления m/{n}! = {result}")
