sentence = input("Введите текст: ")


def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word


result = find_longest_word(sentence)

print("Самое длинное слово в предложении:", result)
