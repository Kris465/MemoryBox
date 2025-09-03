def find_first_duplicate_pair(sentence):

    for i in range(len(sentence) - 1):
        if sentence[i] == sentence[i + 1]:
            return (i + 1, i + 2)

    return None


sentence = input("Введите предложение: ")
result = find_first_duplicate_pair(sentence)

if result:
    print(f"Первая пара одинаковых соседних символов\
        находится на позициях: {result[0]} и {result[1]}")
else:
    print("Пары одинаковых соседних символов не найдены.")
