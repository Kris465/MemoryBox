
sentence1 = "слово1 слово2 слово3 слово1"
sentence2 = "слово2 слово4 слово5"


unique_words1 = set(sentence1.split())
words2 = set(sentence2.split())
result = {word: word in words2 for word in unique_words1}
print("9.181", result)
