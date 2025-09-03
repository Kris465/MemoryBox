def sum_max_min_digits_is_multiple(n, a):
    digits = str(n)

    max_digit = max(digits)
    min_digit = min(digits)

    total_sum = int(max_digit) + int(min_digit)

    return total_sum % a == 0


number = 123456789
divisor = 5
result = sum_max_min_digits_is_multiple(number, divisor)
print(result)
