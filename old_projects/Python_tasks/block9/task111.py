def modify_word(word):
    length = len(word)
    if length % 2 == 1:
        mid_index = length // 2
        return word[:mid_index] + word[mid_index + 1:]
    else:
        mid_index1 = length // 2 - 1
        mid_index2 = length // 2
        return word[:mid_index1] + word[mid_index2 + 1:]

slovo = input("Введите слово: ")
modified_word = modify_word(slovo)
print("Измененное слово:", modified_word)
