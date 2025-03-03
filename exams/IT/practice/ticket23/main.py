import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"Шаг {i+1}: {arr}\n")

        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


size = int(input("Введите размер массива: "))

array = [random.randint(1, 100) for _ in range(size)]
print("Исходный массив:", array)

bubble_sort(array)

print("\nОтсортированный массив:", array)
