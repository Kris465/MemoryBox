def number_properties(n):
    digits = str(n)
    count = len(digits)
    sum_digits = sum(map(int, digits))
    product_digits = eval('*'.join(digits))
    average_digits = sum_digits / count
    sum_squares = sum(int(d)**2 for d in digits)
    sum_cubes = sum(int(d)**3 for d in digits)
    first_digit = int(digits[0])
    last_digit = int(digits[-1])
    sum_first_last = first_digit + last_digit
    return count, sum_digits, product_digits, average_digits, sum_squares, sum_cubes, first_digit, sum_first_last

# Пример использования
n = 12345
count, sum_digits, product_digits, average_digits, sum_squares, sum_cubes, first_digit, sum_first_last = number_properties(n)
print(f"Количество цифр: {count}")
print(f"Сумма цифр: {sum_digits}")
print(f"Произведение цифр: {product_digits}")
print(f"Среднее арифметическое цифр: {average_digits:.2f}")
print(f"Сумма квадратов цифр: {sum_squares}")
print(f"Сумма кубов цифр: {sum_cubes}")
print(f"Первая цифра: {first_digit}")
print(f"Сумма первой и последней цифр: {sum_first_last}")
