classes = []
for parallel in range(1, 12):
    print(f"Введите количество учеников в параллели {parallel} для классов А, \
          Б, В и Г через пробел:")
    row = list(map(int, input().split()))
    if len(row) != 4:
        print("Ошибка: введено неверное количество классов. Должно быть 4.")
        continue
    classes.append(row)

for i, parallel in enumerate(classes):
    min_class = min(parallel)
    print(f"Самый малочисленный класс в параллели {i + 1}: {min_class} \
        учеников.")


classes_by_letter = list(zip(*classes))
for i, letter in enumerate('А Б В Г'.split()):
    min_class = min(classes_by_letter[i])
    print(f"Самый малочисленный класс с буквой {letter}: {min_class} учеников")
