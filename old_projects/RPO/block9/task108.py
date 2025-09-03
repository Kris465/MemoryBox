def correct_word(word):
    corrections = {
        "глинянный": "глиняный",
        "граффика": "графика"
    }
    return corrections.get(word, word)

word1 = "глинянный"
word2 = "граффика"

corrected_word1 = correct_word(word1)
corrected_word2 = correct_word(word2)

print("Исправленное слово 1:", corrected_word1)
print("Исправленное слово 2:", corrected_word2)
