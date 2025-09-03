def find_max_min_digits(n):
    # Преобразуем число в строку для удобной работы с цифрами
    digits = str(n)
    
    # а) Максимальная цифра
    max_digit = max(int(d) for d in digits)
    
    # б) Минимальная цифра
    min_digit = min(int(d) for d in digits)
    
    return {
        'максимальная_цифра': max_digit,
        'минимальная_цифра': min_digit
    }

# Примеры использования
examples = [
    12345,      # простое число
    999,        # все цифры одинаковые
    1000,       # есть нули
    54321,      # убывающая последовательность
    112233      # повторяющиеся цифры
]

for number in examples:
    result = find_max_min_digits(number)
    print(f"Число: {number}")
    print(f"Результаты:")
    for key, value in result.items():
        print(f"  {key}: {value}")
    print()
