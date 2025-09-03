import math

# Ввод массива
arr = list(map(float, input("Введите массив вещественных чисел через пробел: \
                            ").split()))

# а) Каждый элемент, больший 10, заменить его квадратным корнем
for i in range(len(arr)):
    if arr[i] > 10:
        arr[i] = math.sqrt(arr[i])


for i in range(1, len(arr), 2):
    arr[i] = abs(arr[i])

# Вывод результата
print("Изменённый массив:", arr)
