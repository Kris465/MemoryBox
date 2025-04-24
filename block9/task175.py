def unique_words(sentence):
    words = sentence.split()

    word_count = {}

    for word in words:
        word_lower = word.lower()
        if word_lower in word_count:
            word_count[word_lower] += 1
        else:
            word_count[word_lower] = 1

    unique_words_list = [word for word, count in word_count.items() if count == 1]

    return unique_words_list


sentence = "мама мыла раму и мама ела яблоко"
result = unique_words(sentence)

print("Слова, которые встречаются в предложении ровно один раз:", result)
