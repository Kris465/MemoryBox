def correct_word(word):
    return word.replace("рпроцессо", "процессор")


error_word = "рпроцессо"
corrected_word = correct_word(error_word)
print("Исправленное слово:", corrected_word)
