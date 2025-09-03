a = int(input("Введите начало последовательности: "))
b = int(input("Введите конец последовательности: "))
n = int(input("Введите число n: "))


def find_closest(sorted_sequence, n):
    closest_num = sorted_sequence[0]
    closest_index = 1
    min_diff = abs(sorted_sequence[0] - n)
    for i in range(len(sorted_sequence)):
        current_diff = abs(sorted_sequence[i] - n)
        if current_diff < min_diff:
            min_diff = current_diff
            closest_num = sorted_sequence[i]
            closest_index = i + 1
    return closest_index, closest_num


sequence = []
for i in range(a, b):
    sequence.extend([i])
index, value = find_closest(sequence, n)
print(f"Ближайший элемент: {value} (порядковый номер: {index})")
