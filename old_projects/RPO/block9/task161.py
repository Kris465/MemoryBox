def unique_letters(word1, word2, word3):
    def count_letters(word):
        letter_count = {}
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        return letter_count

    count1 = count_letters(word1)
    count2 = count_letters(word2)
    count3 = count_letters(word3)

    def unique_with_counts():
        unique = []
        all_letters = set(word1 + word2 + word3)

        for letter in all_letters:
            if (letter in count1 and letter not in count2 and
                letter not in count3) or \
               (letter in count2 and letter not in count1 and
                letter not in count3) or \
               (letter in count3 and letter not in count1 and
                    letter not in count2):
                unique.append(letter)

        return ''.join(unique)

    def unique_without_counts():
        unique = []
        unique_set1 = set(word1)
        unique_set2 = set(word2)
        unique_set3 = set(word3)

        for letter in (unique_set1 | unique_set2 | unique_set3):
            if (letter in unique_set1 and letter not in unique_set2 and
                letter not in unique_set3) or \
               (letter in unique_set2 and letter not in unique_set1 and
                letter not in unique_set3) or \
               (letter in unique_set3 and letter not in unique_set1 and
                    letter not in unique_set2):
                unique.append(letter)

        return ''.join(unique)

    return unique_with_counts(), unique_without_counts()


word1 = "программирование"
word2 = "грамма"
word3 = "информация"

result_with_counts, result_without_counts = unique_letters(word1, word2, word3)
print("Буквы которые есть лишь в одном слов c повторений:", result_with_counts)
print("Буквы которые одном словt без повторений:", result_without_counts)
