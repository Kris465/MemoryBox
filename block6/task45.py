def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_of_three_numbers(a, b, c):
    return gcd(gcd(a, b), c)


# Пример использования
a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))
c = int(input("Введите третье натуральное число: "))

result = gcd_of_three_numbers(a, b, c)
print(f"Наибольший общий делитель чисел {a}, {b} и {c} равен {result}.")
