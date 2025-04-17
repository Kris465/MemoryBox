sentence = input("ВВедите предложение: ")

words1 = sentence.split()
print("a)", len(words1))

sentence_with_spaces = sentence.strip()
words2 = sentence_with_spaces.split()
print("б)", len(words2))
