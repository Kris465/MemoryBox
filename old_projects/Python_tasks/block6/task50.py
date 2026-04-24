def check_digit_in_number(num: int, digit: int) -> bool:
    """Проверяет, есть ли цифра digit в числе num."""
    return str(digit) in str(num)


def check_digit_not_in_number(num: int, digit: int) -> bool:
    """Проверяет, нет ли цифры digit в числе num."""
    return str(digit) not in str(num)


def check_digit_occurrences(num: int, digit: int, k: int) -> bool:
    """Проверяет, встречается ли цифра digit в числе num более k раз."""
    return str(num).count(str(digit)) > k


def check_digits_in_number(num: int, digit_a: int, digit_b: int) -> bool:
    """Проверяет, есть ли цифры digit_a и digit_b в числе num."""
    return str(digit_a) in str(num) and str(digit_b) in str(num)


number = 1234567890
a = 5
b = 2
k = 1

print(check_digit_in_number(number, a))
print(check_digit_not_in_number(number, b))
print(check_digit_occurrences(number, a, k))
print(check_digits_in_number(number, a, b))
