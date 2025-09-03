import math


def is_prime_recursive(n, divisor=2):
    # Если число меньше или равно 1, оно не простое
    if n <= 1:
        return False

    if divisor > math.isqrt(n):
        return True
    # Если нашли делитель, число не простое
    if n % divisor == 0:
        return False
    # Пробуем следующий возможный делитель
    return is_prime_recursive(n, divisor + 1)


number = int(input("Введите число для проверки: "))
if is_prime_recursive(number):
    print(f"Число {number} простое.")
else:
    print(f"Число {number} не простое.")
