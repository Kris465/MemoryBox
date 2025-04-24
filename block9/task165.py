def reverse_sentence(sentence):

    words = sentence.split()

    reversed_words = words[::-1]

    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


sentence = "мама мыла раму"
result = reverse_sentence(sentence)
print("Предложение в обратном порядке слов:", result)
