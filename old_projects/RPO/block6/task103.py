import math


def reduce_fraction(a, b):
    gcd = math.gcd(a, b)
    return a // gcd, b // gcd


a = 10
b = 80
p, q = reduce_fraction(a, b)
print(f"Сокращённая дробь: {p}/{q}")
