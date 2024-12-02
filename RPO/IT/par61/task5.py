def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


# Пример использования
a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))
print(f"НОД({a}, {b}) = {gcd_recursive(a, b)}")


def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Пример использования
print(f"НОД({a}, {b}) = {gcd_iterative(a, b)}")
