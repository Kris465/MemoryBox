from random import randint


def reverse_selection(arr, k, m):
    arr[k:m+1] = reversed(arr[k:m+1])
    return arr


array = [randint(0, 10)for _ in range(10)]
k = int(input("введите индекс K: "))
m = int(input("введите индекс M: "))
print("исходный массив:", array)
print("массив после реверса секции:", reverse_selection(array, k, m))
