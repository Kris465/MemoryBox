def find_eight_position(n):
    # Преобразуем число в строку
    num_str = str(n)
    
    # Находим первую встреченную цифру 8 справа налево
    try:
        # rindex ищет с конца строки
        pos = len(num_str) - num_str.rindex('8')
        return pos
    except ValueError:
        # Если цифра 8 не найдена
        return 0

# Примеры использования
examples = [
    12345,      # нет цифры 8
    123488,     # несколько цифр 8
    812345,     # цифра 8 в начале
    12345,      # повторный пример для проверки
    888888      # все цифры 8
]

for number in examples:
    position = find_eight_position(number)
    print(f"Число: {number}")
    print(f"Позиция цифры 8 (от конца): {position}\n")
