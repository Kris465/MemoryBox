def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def coprime_numbers_less_than_n(n, p):
    result = []
    for i in range(1, n):
        if gcd(i, p) == 1:
            result.append(i)
    return result


n = int(input("Введите значение n: "))
p = int(input("Введите значение p: "))
coprimes = coprime_numbers_less_than_n(n, p)
print("Натуральные числа, меньшие n и взаимно простые с p:")
print(coprimes)
