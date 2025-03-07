def count_first_digit(n):
    # Преобразуем число в строку
    num_str = str(n)
    # Находим первую цифру и считаем её вхождения
    first_digit = num_str[0]
    return num_str.count(first_digit)

# Примеры использования
examples = [
    12345,      # простое число
    11111,      # все цифры одинаковые
    1000,       # есть нули
    12345,      # повторный пример для проверки
    999999      # все цифры одинаковые
]

for number in examples:
    count = count_first_digit(number)
    print(f"Число: {number}")
    print(f"Количество встреч первой цифры: {count}\n")
    