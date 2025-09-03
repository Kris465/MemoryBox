sequence = []
while True:
    num = int(input("Введите число (для заврешения введите -1): "))
    if num == -1:
        break
    sequence.append(num)


if len(sequence) < 2:
    print("Ошибка, последовательность должна содержать не менее двух чисел.")
else:
    found = False
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            print(f"Найдена пара одинаковых соседних чисел: {sequence[i - 1]}n\
            и {sequence[i]}")
            print(f"Порядковые номера: {i} и {i + 1}")
            found = True
            break

    if not found:
        print("В последовательности нет пар одинаковых соседних чисел. ")
