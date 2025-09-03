def find_odd_neighbors(arr):
    n = len(arr)

    for i in range(n - 1):
        if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0:
            return f"Первая пара соседних нечетных элементов находится \
                на позициях {i} и {i + 1}: ({arr[i]}, {arr[i + 1]})"

    return "Нет соседних нечетных элементов."


arr = [2, 3, 5, 8, 11, 13]
result = find_odd_neighbors(arr)
print(result)
