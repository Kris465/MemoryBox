def is_sum_divisible(n, a):
    digits = str(n)
    max_digit = max(digits)
    min_digit = min(digits)
    return (int(max_digit) + int(min_digit)) % a == 0

# Пример использования
n = 12345
a = 5
print(is_sum_divisible(n, a))
