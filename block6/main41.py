def find_max_and_min_digits(n):
    # Преобразуем число в строку для удобства итерации по цифрам
    digits = [int(d) for d in str(n)]
    
    # Инициализируем переменные для хранения максимальных и минимальных цифр
    max1 = max2 = -1
    min1 = min2 = 10
    
    # Проходим по всем цифрам числа
    for digit in digits:
        # Находим две максимальные цифры
        if digit > max1:
            max2 = max1
            max1 = digit
        elif digit > max2:
            max2 = digit
        
        # Находим две минимальные цифры
        if digit < min1:
            min2 = min1
            min1 = digit
        elif digit < min2:
            min2 = digit
    
    return (max1, max2), (min1, min2)

# Пример использования
n = 123456789
(max1, max2), (min1, min2) = find_max_and_min_digits(n)
print(f"Две максимальные цифры: {max1}, {max2}")
print(f"Две минимальные цифры: {min1}, {min2}")
