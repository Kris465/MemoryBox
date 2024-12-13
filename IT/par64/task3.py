from random import randint


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
        if not swapped:
            break
        return arr


a = [randint(1, 100) for i in range(30)]
print(a)
print(bubbleSort(a))
