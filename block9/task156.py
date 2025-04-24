word1 = "информация"
word2 = "процессор"
result = ["да" if letter in word2 else "нет" for letter in word1]
print("Результат:", " ".join(result))
