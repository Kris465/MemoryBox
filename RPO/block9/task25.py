from collections import Counter


def can_form_word(source, target):
    source_count = Counter(source)
    target_count = Counter(target)

    for letter in target_count:
        if target_count[letter] > source_count.get(letter, 0):
            return False
    return True


source_word = "информатика"
word1 = "форма"
word2 = "тик"

if can_form_word(source_word, word1) and can_form_word(source_word, word2):
    print(f"Слова '{word1}' и '{word2}' можно составить из '{source_word}'.")
else:
    print(f"Слова '{word1}' и '{word2}' нельзя составить из '{source_word}'.")
