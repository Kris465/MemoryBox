def count_min_digit(n):
    # Преобразуем число в строку и находим минимальную цифру
    num_str = str(n)
    min_digit = min(num_str)
    # Считаем количество вхождений минимальной цифры
    return num_str.count(min_digit)

# Примеры использования
examples = [
    102200,    # 3 встречи цифры 0
    40330,     # 2 встречи цифры 0
    10345,     # 1 встреча цифры 0
    999999,    # все цифры одинаковые
    12345      # повторный пример для проверки
]

for number in examples:
    count = count_min_digit(number)
    print(f"Число: {number}")
    print(f"Количество встреч минимальной цифры: {count}\n")
