import bisect

def closest_element(sequence, n):
    # Найти индекс, где n должен находиться в последовательности
    index = bisect.bisect_left(sequence, n)

    # Проверяем ближайшие элементы
    if index == 0:
        # n меньше всего элемента в последовательности
        return 0, sequence[0]
    elif index == len(sequence):
        # n больше всех элементов в последовательности
        return len(sequence) - 1, sequence[-1]
    else:
        # n находится между двумя соседними элементами
        before = sequence[index - 1]
        after = sequence[index]

        # Определяем, какой элемент ближе к n
        if abs(before - n) <= abs(after - n):
            return index - 1, before
        else:
            return index, after

# Пример использования
sequence = [1.0, 2.5, 3.7, 4.8, 5.1, 6.3, 7.9, 8.2, 9.5, 10.0, 11.3, 12.4, 13.5, 14.1, 15.9]
n = 10.5

# Находим ближайший элемент
index, value = closest_element(sequence, n)
print(f'Ближайший элемент к {n}: индекс {index}, значение {value}')
