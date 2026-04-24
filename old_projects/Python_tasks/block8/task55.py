def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input("Введите натуральное число n: "))
coprime_numbers = [i for i in range(1, n) if gcd(n, i) == 1]

print("Числа, меньшие n и взаимно простые с ним:")
print(coprime_numbers)
