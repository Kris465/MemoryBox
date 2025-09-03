def find_word_starting_with_k(sentence):
    words = sentence.split()
    for word in words:
        if word.lower().startswith('к'):
            return word
    return None


sentence = "мама мыла раму кот еда"
result = find_word_starting_with_k(sentence)

if result:
    print("Найдено слово, начинающееся на букву 'к':", result)
else:
    print("Слово, начинающееся на букву 'к', не найдено.")
