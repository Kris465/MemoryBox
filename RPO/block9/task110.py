def modify_word(word):
    if 'о' in word:
        word = word.replace('о', '', 1)
    if 'л' in word:
        word = word[::-1].replace('л', '', 1)[::-1]
    return word


slovo = input("Введите слово: ")
modified_word = modify_word(slovo)
print("Измененное слово:", modified_word)
