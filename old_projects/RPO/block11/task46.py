arr = list(map(float, input(
    "Введите массив вещественных чисел через пробел: ").split()))

for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = abs(arr[i])

for i in range(1, len(arr), 2):
    if arr[i] >= 0:
        arr[i] = (arr[i]) ** 0.5
    else:
        pass

print("Изменённый массив:", arr)
