def stone_sort(arr):
    n = len(arr)
    for i in range(n):
        max_index = 0
        for j in range(1, n - i):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[max_index], arr[n - i - 1] = arr[n - i - 1], arr[max_index]
    return arr


array = [3, 1, 4, 2, 5]
sorted_array = stone_sort(array)
print("Отсортированный массив методом камня:", sorted_array)
