def recursive_max_index(arr, idx=0):
    if idx >= len(arr) - 1:
        return idx
    else:
        max_idx_left = recursive_max_index(arr, idx + 1)
        if arr[idx] > arr[max_idx_left]:
            return idx
        else:
            return max_idx_left


array = [3, 5, 1, 8, 4, 9, 2]
max_index = recursive_max_index(array)
print(f"Индекс максимального элемента массива: {max_index}")
