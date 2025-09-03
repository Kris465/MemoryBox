def to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return to_binary(n // 2) + str(n % 2)


# Пример использования
number = int(input("Введите число для перевода в двоичную систему: "))
print(f"Число {number} в двоичной системе: {to_binary(number)}")
