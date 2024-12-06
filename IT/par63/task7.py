from random import randint


def reverse_half(arr):
    mid = len(arr) // 2
    arr[:mid] = reversed(arr[:mid])
    arr[mid:] = reversed(arr[mid:])

    return arr


array = [randint(0, 10) for _ in range(10)]
print("Исходный массив:", array)
print("Массив после реверса половин:", reverse_half(array))
