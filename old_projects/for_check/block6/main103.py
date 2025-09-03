import math

def reduce_fraction(a, b):
    # Находим наибольший общий делитель (НОД) чисел a и b
    gcd_value = math.gcd(a, b)
    # Сокращаем дробь, деля числитель и знаменатель на НОД
    p = a // gcd_value
    q = b // gcd_value
    return p, q

# Пример использования
a = 24
b = 36
p, q = reduce_fraction(a, b)
print(f"Сокращенная дробь: {p}/{q}")
