def correct_word(word):
    return word.replace("килбайот", "килобайт")


error_word = "килбайот"
corrected_word = correct_word(error_word)
print("Исправленное слово:", corrected_word)
