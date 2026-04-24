word = "пример"
word = list(word)
word[2], word[-1] = word[-1], word[2]
word = "".join(word)
print(word)
