
first_occurrence_index = -1
index = 0


while True:
    num = int(input())

    if num == 100:
        break

    if num == 77 and first_occurrence_index == -1:
        first_occurrence_index = index

    index += 1


if first_occurrence_index != -1:
    print("Первое вхождение числа 77 находится на позиции:",
          first_occurrence_index + 1)
else:
    print("Число 77 не найдено в последовательности.")
