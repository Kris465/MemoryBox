def max_sum_neighbors(sequence):
    return max(sequence[i] + sequence[i+1] for i in range(len(sequence) - 1))


sequence = [1, 3, 5, 2, 4]
result = max_sum_neighbors(sequence)
print(f"Максимальная сумма двух соседних чисел: {result}")


def min_sum_neighbors(sequence):
    return min(sequence[i] + sequence[i+1] for i in range(len(sequence) - 1))


sequence = [1, 3, 5, 2, 4]
result = min_sum_neighbors(sequence)
print(f"Минимальная сумма двух соседних чисел: {result}")


def max_sum_neighbors_indices(sequence):
    sums = [sequence[i] + sequence[i+1] for i in range(len(sequence) - 1)]
    max_sum = max(sums)
    return sums.index(max_sum) + 1, sums.index(max_sum) + 2


sequence = [1, 3, 5, 2, 4]
result = max_sum_neighbors_indices(sequence)
print(f"Номера пары с максимальной суммой: {result}")


def min_sum_neighbors_indices(sequence):
    sums = [sequence[i] + sequence[i+1] for i in range(len(sequence) - 1)]
    min_sum = min(sums)
    return len(sums) - sums[::-1].index(min_sum), len(sums)
    -sums[::-1].index(min_sum) + 1


sequence = [1, 3, 5, 2, 4]
result = min_sum_neighbors_indices(sequence)
print(f"Номера пары с минимальной суммой: {result}")
