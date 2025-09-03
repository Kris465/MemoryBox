def find_positions(n):
    # Преобразуем число в строку
    num_str = str(n)
    
    # Инициализируем переменные для хранения позиций
    max_from_start = 0
    max_from_end = 0
    min_from_start = 0
    min_from_end = 0
    
    # Один цикл для поиска всех позиций
    for i in range(len(num_str)):
        if num_str[i] == max(num_str):
            max_from_start = i + 1
            max_from_end = len(num_str) - i
        if num_str[i] == min(num_str):
            min_from_start = i + 1
            min_from_end = len(num_str) - i
    
    return {
        'макс_от_начала': max_from_start,
        'макс_от_конца': max_from_end,
        'мин_от_начала': min_from_start,
        'мин_от_конца': min_from_end
    }

# Примеры использования
examples = [
    12345,      # простое число
    54321,      # убывающая последовательность
    987654,     # все цифры различны
    12345       # повторный пример для проверки
]

for number in examples:
    result = find_positions(number)
    print(f"\nАнализ числа {number}:")
    for key, value in result.items():
        print(f"  {key}: {value}")
