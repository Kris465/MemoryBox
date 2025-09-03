def find_leftmost_digit(number):

    digits = list(str(number))

    max_index = digits.index(max(digits))
    min_index = digits.index(min(digits))

    if max_index < min_index:
        return f'Максимальная цифра ({max(digits)}) расположена \
    левее минимальной.'
    else:
        return f'Минимальная цифра ({min(digits)}) расположена \
    левее максимальной.'
