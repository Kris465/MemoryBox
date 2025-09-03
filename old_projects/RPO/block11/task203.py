def print_after_first_pair(arr):
    n = len(arr)

    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            result = arr[i + 2:]
            return result
    return []


arr = list(map(int, input("Введите массив через пробел: ").split()))
output = print_after_first_pair(arr)
if output:
    print("Следующие элементы после первой пары:", output)
else:
    print("Нет соседних одинаковых элементов.")