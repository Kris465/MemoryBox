def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def unique_prime_factors(n):
    return list(set(prime_factors(n)))


n = int(input("Введите натуральное число n: "))

print("Разложение на простые множители (каждый множитель один раз):")
print(unique_prime_factors(n))

print("Разложение на простые множители\
    (каждый множитель столько раз, сколько раз он входит):")
print(prime_factors(n))
