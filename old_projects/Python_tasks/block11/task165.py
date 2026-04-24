def insert_numbers(arr, n, m):
    i = 0
    while i < len(arr):
        if arr[i] > n:
            arr.insert(i, n)
            i += 1
        i += 1

    i = 0
    while i < len(arr):
        if arr[i] < m:
            arr.insert(i + 1, m)
            i += 1
        i += 1

    return arr


arr = [list(map(int, input("Введите массив: ").split()))]
n = int(input("Введите n"))
m = int(input("Введите m"))
print(insert_numbers(arr, n, m))
