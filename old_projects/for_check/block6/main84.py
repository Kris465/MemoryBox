def which_come_first(n):
    digits = str(n)
    max_digit = max(digits)
    min_digit = min(digits)
    return "Максимальная цифра" if digits.index(max_digit) < digits.index(min_digit) else "Минимальная цифра"


n = 12345
print(which_come_first(n))
