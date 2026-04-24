def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


number = 12345
print(f"Сумма цифр числа {number}: {sum_digits(number)}")


def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)


number = 12345
print(f"Количество цифр в числе {number}: {count_digits(number)}")
