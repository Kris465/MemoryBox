from random import randint

spisok1 = []
for i in range(10):
    spisok1.append(randint(1, 10))

print(*spisok1)

spisok1.sort()
print(*spisok1)
print(len(set(spisok1)))
