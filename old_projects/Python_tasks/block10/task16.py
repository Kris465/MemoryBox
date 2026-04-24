def is_prime(n):
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


twin_primes = []


for num in range(3, 200):
    if is_prime(num) and is_prime(num + 2):
        twin_primes.append((num, num + 2))

for pair in twin_primes:
    print(pair)
