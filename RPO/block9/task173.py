def is_longest_word_longer_than_ten(sentence):

    words = sentence.split()

    longest_word = max(words, key=len)

    return len(longest_word) > 10


sentence = "мама мыла раму и очень долго думала о программировании"
result = is_longest_word_longer_than_ten(sentence)

if result:
    print("Самое длинное слово имеет больше 10 символов.")
else:
    print("Самое длинное слово не имеет больше 10 символов.")
