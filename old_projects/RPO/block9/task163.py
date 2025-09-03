def unique_letters(word1, word2, word3):
    all_letters = word1 + word2 + word3
    letter_count = {}

    for letter in all_letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    unique = [letter for letter, count in letter_count.items() if count == 1]

    return ''.join(unique)


word1 = "программирование"
word2 = "грамма"
word3 = "информация"

result = unique_letters(word1, word2, word3)
print("Неповторяющиеся буквы в словах:", result)
