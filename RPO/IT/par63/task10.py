from random import randint


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(arr):
    return [x for x in arr if is_prime(x)]


array = [randint(0, 100) for _ in range(20)]
print("Массив:", array)
print("Простые числа в массиве:", find_primes(array))
