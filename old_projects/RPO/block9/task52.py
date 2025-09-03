sentence = input("Введите предложение: ")
char_to_find = input("Укажите символ для поиска: ")

positions = []
for i in range(len(sentence)):
    if sentence[i] == char_to_find:
        positions.append(i)

if len(positions) > 0:
    print(f"Вхождение символа '{char_to_find}' в предложении:")
    for pos in positions:
        print(pos)
else:
    print(f"Символ '{char_to_find}' отсутствует в предложении.")
