def sort_by_last_digit(arr):
    return sorted(arr, key=lambda x: x % 10)


array = [23, 45, 12, 34, 56]
sorted_array = sort_by_last_digit(array)
print("Отсортированный массив по последней цифре:", sorted_array)
