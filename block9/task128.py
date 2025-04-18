def rearrange_word(word, k):
    if k < 1 or k > len(word):
        return "Некорректное значение k."
    return word[1:k] + word[0] + word[k:]


word = input("Введите слово: ")
k = int(input("Введите номер позиции (k): "))
modified_word = rearrange_word(word, k)
print("Измененное слово:", modified_word)
