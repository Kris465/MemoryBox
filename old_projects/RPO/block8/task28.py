def is_prime(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_numbers_with_six_divisors(start, end):
    primes = [p for p in range(2, int(end**(1/3)) + 1) if is_prime(p)]
    result = set()

    for p in primes:
        for q in primes:
            if p != q and p*q**2 >= start and p*q**2 <= end:
                result.add(p*q**2)

    return sorted(result)


start = 200
end = 500
numbers = find_numbers_with_six_divisors(start, end)

print
("Все числа с шестью делителями в диапазоне от {} до {}:".format(start, end))
for number in numbers:
    print(number)
