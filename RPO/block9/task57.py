sentence = input()
for i in range(1, len(sentence), 2):
    if sentence[i] == 'и' or sentence[i] == 'И':
        print(sentence[i])
