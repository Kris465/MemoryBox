def find_min_max_indices(arr):
    min_value = min(arr)

    max_value = max(arr)

    min_indices = [i for i, x in enumerate(arr) if x == min_value]
    max_indices = [i for i, x in enumerate(arr) if x == max_value]

    return min_indices, max_indices


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 1]
min_indices, max_indices = find_min_max_indices(arr)
print("Индексы минимальных элементов:", min_indices)
print("Индексы максимальных элементов:", max_indices)
