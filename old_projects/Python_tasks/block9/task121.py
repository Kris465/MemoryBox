def insert_letter(word, position, letter):
    if position < 0 or position >= len(word) - 1:
        return "Некорректный номер позиции."
    return word[:position + 1] + letter + word[position + 1:]


word = input("Введите слово, оканчивающееся символом '_': ")
position = int(input("Введите номер позиции (начиная с 0): "))
letter = input("Введите букву для вставки: ")

modified_word = insert_letter(word, position, letter)
print("Измененное слово:", modified_word)
