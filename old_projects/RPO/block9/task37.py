word = "абвгде"
half = len(word) // 2
result1 = word[half:] + word[:half]
print("Без цикла", result1)

result2 = ""
for i in range(half, len(word)):
    result2 += word[i]


for i in range(half):
    result2 += word[i]


print("С циклом", result2)
