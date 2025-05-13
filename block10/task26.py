def gcd(a, b):
    """
    Функция для нахождения наибольшего общего делителя (НОД) двух чисел
    с использованием алгоритма Евклида.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))


gcd_ab = gcd(a, b)


result = gcd(gcd_ab, c)

print(f"НОД({a}, {b}, {c}) = {result}")
