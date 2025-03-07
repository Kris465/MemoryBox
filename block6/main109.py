def alternating_sum_of_digits(n):
    digits = str(n)  # Преобразуем число в строку для доступа к цифрам
    sum_digits = 0
    for i, digit in enumerate(digits):
        sign = (-1) ** i  # Чередование знака: +, -, +, -, ...
        sum_digits += int(digit) * sign
    return sum_digits

# Пример использования
number = 12345
result = alternating_sum_of_digits(number)
print(f"Знакочередующаяся сумма цифр числа {number} равна {result}")
