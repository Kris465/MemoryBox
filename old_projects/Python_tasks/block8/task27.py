def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_numbers_with_five_divisors(limit):
    result = []
    primes = [p for p in range(2, limit // 4 + 1) if is_prime(p)]
    for prime in primes:
        candidate = prime ** 4
        if candidate <= limit:
            result.append(candidate)
    return result


numbers = find_numbers_with_five_divisors(300)
print(numbers)
