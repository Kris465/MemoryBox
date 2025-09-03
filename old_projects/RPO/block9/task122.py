def insert_after_i(word, letter):
    index = word.find('и')
    if index != -1:
        return word[:index + 1] + letter + word[index + 1:]
    return word


word = input("Введите слово, оканчивающееся символом '_': ")
letter = input("Введите букву для вставки: ")

modified_word = insert_after_i(word, letter)
print("Измененное слово:", modified_word)
