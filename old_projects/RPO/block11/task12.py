def fill_divisible_by_13_or_17(limit, count):
    divisible_numbers = []
    num = limit

    while len(divisible_numbers) < count:
        if num % 13 == 0 or num % 17 == 0:
            divisible_numbers.append(num)
        num += 1

    return divisible_numbers


result_a = fill_divisible_by_13_or_17(300, 20)
print("Массив чисел, делящихся на 13 или 17:", result_a)


def is_prime(num):
    """Проверка числа на простоту"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes(count):
    primes = []
    num = 2

    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes


result_b = generate_primes(30)
print("Массив из тридцати первых простых чисел:", result_b)
