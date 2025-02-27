def find_eight_position(n):
    num_str = str(n)
    
    try:
        # rindex ищет с конца строки
        pos = len(num_str) - num_str.rindex('8')
        return pos
    except ValueError:
        # Если цифра 8 не найдена
        return 0

examples = [
    12345,
    123488,
    812345,
    12345,
    888888      

for number in examples:
    position = find_eight_position(number)
    print(f"Число: {number}")
    print(f"Позиция цифры 8 (от конца): {position}\n")
]
