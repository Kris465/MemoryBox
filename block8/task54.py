def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_divisors(n):
    divisors = [i for i in range(2, n + 1) if n % i == 0 and is_prime(i)]
    return divisors


n = int(input("Введите натуральное число n: "))
print("Простые делители числа:", prime_divisors(n))
