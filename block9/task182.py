sentence1 = "слово1 слово2 слово3 слово1"
sentence2 = "слово2 слово4 слово5"


words1 = sentence1.split()
words2 = sentence2.split()
unique_to_sentence1 = [word for word in words1 if word not in words2]
unique_to_sentence2 = [word for word in words2 if word not in words1]
result = unique_to_sentence1 + unique_to_sentence2
print("9.182", result)
