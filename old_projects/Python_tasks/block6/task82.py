def is_difference_even(n):
    digits = str(n)
    max_digit = max(digits)
    min_digit = min(digits)
    return (int(max_digit) - int(min_digit)) % 2 == 0


n = 12345
print(is_difference_even)
