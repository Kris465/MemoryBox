word = "пример"
word = list(word)
word[1], word[4] = word[4], word[1]
word = "".join(word)
print(word)
