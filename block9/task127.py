def correct_word(word):
    return word.replace("иинформаця", "информация")


error_word = "иинформаця"
corrected_word = correct_word(error_word)
print("Исправленное слово:", corrected_word)
