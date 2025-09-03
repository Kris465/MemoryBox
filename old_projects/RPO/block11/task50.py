# Ввод массива
arr = list(map(float, input("Введите массив вещественных чисел через пробел: \
                            ").split()))

# Ввод номеров k1, а также чисел n, a, b
k1 = int(input("Введите номер k1 (начиная с 1): "))
n = float(input("Введите число n: "))
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

# Проверка корректности номера k1
if not (1 <= k1 <= len(arr)):
    print("Номер k1 выходит за границы массива.")
else:
    idx_k1 = k1 - 1

    # а) Из всех положительных элементов вычесть элемент с номером k1,
    # из всех отрицательных — число n. Нулевые оставить без изменения.
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] -= arr[idx_k1]
        elif arr[i] < 0:
            arr[i] -= n

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] += n
        elif arr[i] > 0:
            arr[i] -= a
        elif arr[i] < 0:
            arr[i] += b

# Вывод результата
print("Изменённый массив:", arr)
