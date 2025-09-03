def analyze_number(n):
    # Преобразуем число в строку для удобной работы с цифрами
    digits = str(n)
    
    # а) Количество цифр 3
    count_3 = sum(1 for digit in digits if digit == '3')
    
    # б) Количество последней цифры
    last_digit = digits[-1]
    count_last = sum(1 for digit in digits if digit == last_digit)
    
    # в) Количество четных цифр (без составного условия)
    count_even = sum(1 for digit in digits if int(digit) % 2 == 0)
    
    # г) Сумма цифр, больших пяти
    sum_greater_5 = sum(int(digit) for digit in digits if int(digit) > 5)
    
    # д) Произведение цифр, больших семи
    product_greater_7 = 1
    for digit in digits:
        if int(digit) > 7:
            product_greater_7 *= int(digit)
    
    # е) Количество цифр 0 и 5
    count_0_5 = sum(1 for digit in digits if digit in '05')
    
    return {
        'количество_3': count_3,
        'количество_последней_цифры': count_last,
        'количество_четных_цифр': count_even,
        'сумма_цифр_больше_5': sum_greater_5,
        'произведение_цифр_больше_7': product_greater_7,
        'количество_0_и_5': count_0_5
    }

# Пример использования
number = 123450
result = analyze_number(number)
print(f"Анализ числа {number}:")
for key, value in result.items():
    print(f"{key}: {value}")
