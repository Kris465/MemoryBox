def sum_last_digits(n, m):
    num_str = str(n)
    last_digits = num_str[-m:]
    return sum(int(digit) for digit in last_digits)


number = 123456789
m = 3
result = sum_last_digits(number, m)
print(f"Сумма последних {m} цифр числа {number}: {result}")
