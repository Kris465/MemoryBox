sentence = input("Введите предложение: ")


chars = list(sentence)


for i in range(len(chars)):
    if (i + 1) % 3 == 0:
        chars[i] = 'а'


result = ''.join(chars)

print("Результат:", result)
