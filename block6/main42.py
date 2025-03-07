def find_digit_positions(n):
    digits = list(map(int, str(n)))  # Преобразуем число в список цифр
    max1_index = max2_index = min1_index = min2_index = -1
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for i in range(len(digits)):
        digit = digits[i]
        # Проверка максимальных цифр
        if digit > max1:
            max2, max2_index = max1, max1_index
            max1, max1_index = digit, i
        elif digit > max2:
            max2, max2_index = digit, i
        
        # Проверка минимальных цифр
        if digit < min1:
            min2, min2_index = min1, min1_index
            min1, min1_index = digit, i
        elif digit < min2:
            min2, min2_index = digit, i

    # Вычисляем порядковые номера от начала и конца
    max1_position_from_start = max1_index + 1
    max2_position_from_start = max2_index + 1
    max1_position_from_end = len(digits) - max1_index
    max2_position_from_end = len(digits) - max2_index

    min1_position_from_start = min1_index + 1
    min2_position_from_start = min2_index + 1
    min1_position_from_end = len(digits) - min1_index
    min2_position_from_end = len(digits) - min2_index

    return {
        "max_digits": {
            "from_start": (max1_position_from_start, max2_position_from_start),
            "from_end": (max1_position_from_end, max2_position_from_end)
        },
        "min_digits": {
            "from_start": (min1_position_from_start, min2_position_from_start),
            "from_end": (min1_position_from_end, min2_position_from_end)
        }
    }


# Пример использования:
n = 27364  # Вводим натуральное число
result = find_digit_positions(n)
print("Максимальные цифры: от начала:", result['max_digits']['from_start'], 
      "от конца:", result['max_digits']['from_end'])
print("Минимальные цифры: от начала:", result['min_digits']['from_start'], 
      "от конца:", result['min_digits']['from_end'])
