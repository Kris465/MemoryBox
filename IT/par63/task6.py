from random import randint


def swap_adjacent(arr):
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


array = [randint(0, 10) for _ in range(10)]
print("Исходный массив: ", array)
print("Массив после перестановки: ", swap_adjacent(array))
