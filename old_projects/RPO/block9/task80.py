sequence = input("Введите последовательность символов: ")

count1 = 1
for i in range(1, len(sequence)):
    if sequence[i] == sequence[0]:
        count1 += 1
    else:
        break
print(count1)

count2 = 1
for i in range(1, len(sequence)):
    if sequence[i] == sequence[0]:
        count2 += 1
    else:
        break
print(count2)
