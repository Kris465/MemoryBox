def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def coprime_divisors(q, p):
    divisors = get_divisors(q)
    result = []
    for divisor in divisors:
        if gcd(divisor, p) == 1:
            result.append(divisor)
    return result


p = int(input("Введите значение p: "))
q = int(input("Введите значение q: "))

coprime_divisors_result = coprime_divisors(q, p)
print("Делители числа q, взаимно простые с p:")
print(coprime_divisors_result)
