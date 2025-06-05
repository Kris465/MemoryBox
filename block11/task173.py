def move_last_to_first(arr):
    if len(arr) <= 1:
        return arr

    last = arr[-1]

    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last

    return arr


arr = [list(map(int, input("Введите массив: ").split()))]
print("До:", arr)
move_last_to_first(arr)
print("После:", arr)
