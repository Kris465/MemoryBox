def check_letters(word1, word2):
    unique_letters = set(word1)

    result = []
    for letter in sorted(unique_letters):
        if letter in word2:
            result.append("да")
        else:
            result.append("нет")

    return ' '.join(result)


word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
print(check_letters(word1, word2))
