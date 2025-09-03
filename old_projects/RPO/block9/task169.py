def analyze_sentence(sentence):
    words = sentence.split()

    same_letter_words = [word for word in words if word[0].lower() == word[-1].lower()]

    three_e_words = [word for word in words if word.lower().count('е') == 3]

    at_least_one_o_words = [word for word in words if 'о' in word.lower()]

    return same_letter_words, three_e_words, at_least_one_o_words

# Пример использования
sentence = "мама мыла раму еда око еее"
same_letter_words, three_e_words, at_least_one_o_words = analyze_sentence(sentence)

print("Слова, начинающиеся и оканчивающиеся на одну и ту же букву:", same_letter_words)
print("Слова, которые содержат ровно три буквы 'е':", three_e_words)
print("Слова, которые содержат хотя бы одну букву 'о':", at_least_one_o_words)
