from random import randint


def reverse_section(arr, k, m):
    arr[k:m+1] = reversed(arr[k:m+1])
    return arr


array = [randint(0, 10) for _ in range(10)]
k = int(input("Введите индекс K: "))
m = int(input("Введите индекс M: "))
print("Исходный массив:", array)
print("Массив после реверса секции:", reverse_section(array, k, m))
