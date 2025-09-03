def count_first_digit(n):
    # Преобразуем число в строку
    num_str = str(n)
    # Находим первую цифру и считаем её вхождения
    first_digit = num_str[0]
    return num_str.count(first_digit)


examples = [
    12345,
    11111,
    1000,
    12345,
    999999
]

for number in examples:
    count = count_first_digit(number)
    print(f"Число: {number}")
    print(f"Количество встреч первой цифры: {count}\n")
