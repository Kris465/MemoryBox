def correct_word(word):
    return word.replace("роцессорп", "процессор")


error_word = "роцессорп"
corrected_word = correct_word(error_word)
print("Исправленное слово:", corrected_word)
