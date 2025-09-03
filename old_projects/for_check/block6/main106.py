def integer_division(a, b):
    count = 0
    while a >= b:
        a -= b
        count += 1
    return count, a

# Пример использования
a = 17
b = 5
quotient, remainder = integer_division(a, b)
print(f"Целочисленное деление {a} на {b} равно {quotient}, остаток равен {remainder}")
