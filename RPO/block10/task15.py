def is_prime(n):
    """Функция, определяющая, является ли число простым."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


three_digit_primes = []
for num in range(100, 1000):
    if is_prime(num):
        three_digit_primes.append(num)

print(three_digit_primes)
