def correct_word(word):
    return word.replace("алигортм", "алгоритм")


error_word = "алигортм"
corrected_word = correct_word(error_word)
print("Исправленное слово:", corrected_word)
