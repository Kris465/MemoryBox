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

# Пример использования функций
number = 1234567890
a = 5
b = 2
k = 1

# a) Определить, есть ли в нем цифра a.
print(check_digit_in_number(number, a))  # True, если 5 есть в числе

# б) Верно ли, что в нем нет цифры b?
print(check_digit_not_in_number(number, b))  # False, если 2 есть в числе

# в) Верно ли, что цифра a встречается в нем более k раз?
print(check_digit_occurrences(number, a, k))  # False, если 5 встречается 1 раз или меньше

# г) Определить, есть ли в нем цифры a и b.
print(check_digits_in_number(number, a, b))  # False, если не обе цифры присутствуют
