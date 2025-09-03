def unique_letters(word1, word2):

    result = []

    for char in word1:
        if char not in word2:
            result.append(char)

    for char in word2:
        if char not in word1:
            result.append(char)

    return ''.join(sorted(result))


word1 = 'процессор'
word2 = 'информация'
print(unique_letters(word1, word2))
