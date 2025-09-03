def find_number_from_factorial(factorial):
    n = 1
    while factorial > 1:
        n += 1
        factorial = factorial // n
    return n

# Пример использования
factorial = 120  # Известный факториал
n = find_number_from_factorial(factorial)
print(f"Число, для которого факториал равен {factorial}, это: {n}")
