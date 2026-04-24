def remove_duplicates(word):
    seen = set()
    result = []
    for char in word:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


slovo = input("Введите слово: ")
modified_word = remove_duplicates(slovo)
print("Измененное слово:", modified_word)
