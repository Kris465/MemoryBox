def find_max_duplicate(arr):
    from collections import Counter

    count = Counter(arr)
    duplicates = [num for num, freq in count.items() if freq > 1]

    if duplicates:
        return max(duplicates)
    else:
        return None


array = [1, 2, 3, 2, 4, 5, 3]
sorted_array = sorted(array)
print("Отсортированный массив:", sorted_array)
max_duplicate = find_max_duplicate(sorted_array)
print("Максимальное число из дубликатов:", max_duplicate)
