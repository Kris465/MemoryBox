word1 = input("Введите слово: ")
word2 = input("Введите слово: ")


def unique_common_letters(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    count1 = {}
    count2 = {}
    for letter in word1:
        count1[letter] = count1.get(letter, 0) + 1
    for letter in word2:
        count2[letter] = count2.get(letter, 0) + 1
    result = []
    for letter in count1:
        if count1[letter] == 1 and letter in count2 and count2[letter] == 1:
            result.append(letter)
    return ' '.join(result)


result = unique_common_letters(word1, word2)
print("Буквы, которые встречаются в обоих словах только один раз:", result)
