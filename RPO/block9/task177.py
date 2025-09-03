def find_duplicate_words(sentence):
    words = sentence.split()
    word_count = {}

    for word in words:
        word_lower = word.lower()
        if word_lower in word_count:
            word_count[word_lower] += 1
        else:
            word_count[word_lower] = 1

    duplicates = [word for word, count in word_count.items() if count == 2]

    return duplicates


sentence = "мама мыла раму мама"
result = find_duplicate_words(sentence)

print("Два одинаковых слова:", result)
