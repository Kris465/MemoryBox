def can_form_word(word1, word2):

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

    def can_form_with_unique_letters():
        for letter in count2:
            if letter not in count1:
                return False
        return True

    def can_form_with_exact_counts():
        for letter in count2:
            if count2[letter] > count1.get(letter, 0):
                return False
        return True

    return can_form_with_unique_letters(), can_form_with_exact_counts()


word1 = input("Введите первое слово ")
word2 = input("Введите второе слово ")

result_unique, result_exact = can_form_word(word1, word2)
print("Можно ли из букв первого слова получить второе (без учета количества):",
      result_unique)
print("Можно ли из букв первого слова получить второе (с учетом количества):",
      result_exact)
