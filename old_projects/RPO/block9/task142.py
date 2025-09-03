def find_max_digit_position(text):
    text = text.lstrip()
    max_digit = -1
    position = -1

    for index, char in enumerate(text):
        if char.isdigit():
            if int(char) > max_digit:
                max_digit = int(char)
                position = index + 1

    return position if position != -1 else None


text = "   Пример текста 3 и 5, а также 7."
position = find_max_digit_position(text)
print("Позиция максимальной цифры:", position)
