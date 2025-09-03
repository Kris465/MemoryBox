def find_duplicate_neighbors(arr):
    n = len(arr)

    for i in range(n - 1):

        if arr[i] == arr[i + 1]:
            return f"Первые одинаковые соседи находятся на \
        индексах {i} и {i + 1}"

    return "Нет соседних одинаковых элементов."


array = [1, 2, 3, 3, 4, 5]
result = find_duplicate_neighbors(array)
print(result)
