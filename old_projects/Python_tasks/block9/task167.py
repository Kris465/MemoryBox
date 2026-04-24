sentence = "привет мир привет Python"
words = [word for word in sentence.split() if word != "привет"]
print("Слова, отличные от 'привет':", " " .join(words))
