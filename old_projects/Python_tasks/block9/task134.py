def rearrange_word(word, k):
    if k < 0 or k >= len(word):
        return "Некорректное значение k."
    return word[:k] + word[-1] + word[k:-1]

word = input("Введите слово: ")
k = int(input("Введите номер позиции k (начиная с 0): "))
modified_word = rearrange_word(word, k)
print("Измененное слово:", modified_word)
