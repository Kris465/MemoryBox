
def alternating_sum_of_digits(n):
    digits = str(n)
    sum_digits = 0
    for i, digit in enumerate(digits):
        sign = (-1) ** i
        sum_digits += int(digit) * sign
    return sum_digits


number = 12345
result = alternating_sum_of_digits(number)
print(f"Знакочередующаяся сумма цифр числа {number} равна {result}")
