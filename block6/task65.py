from random import randint


def find_duplicate_neighbors(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            return i + 1, i + 2
    return None


sequence = [randint(0, 100) for i in range(15)]
result = find_duplicate_neighbors(sequence)
if result is not None:
    print(f'Порядковые номера первой пары одинаковых соседних чисел: {result}')
else:
    print('Нет одинаковых соседних чисел')
