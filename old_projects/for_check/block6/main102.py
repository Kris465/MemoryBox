import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Пример использования
a = 12
b = 18
print(f"Наименьшее общее кратное чисел {a} и {b}: {lcm(a, b)}")
