def binary_to_decimal(binary_str):
    if len(binary_str) == 0:
        return 0
    else:
        return int(binary_str[-1]) + 2 * binary_to_decimal(binary_str[:-1])


# Пример использования
binary_number = input("Введите двоичное число: ")
decimal_number = binary_to_decimal(binary_number)
print(f"Двоичное число {binary_number} в десятичной системе: {decimal_number}")
