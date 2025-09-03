def rearrange_word(word):
    if len(word) > 1:
        return word[-1] + word[:-1]
    return word


word = input("Введите слово: ")
modified_word = rearrange_word(word)
print("Измененное слово:", modified_word)
