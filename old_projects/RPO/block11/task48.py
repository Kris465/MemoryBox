arr = list(map(float, input("Введите массив вещественных \
                            чисел через пробел: ").split()))


k1 = int(input("Введите номер k1 (начиная с 1): "))
k2 = int(input("Введите номер k2 (начиная с 1): "))


if not (1 <= k1 <= len(arr)) or not (1 <= k2 <= len(arr)):
    print("Номера k1 или k2 выходят за границы массива.")
else:

    idx_k1 = k1 - 1
    idx_k2 = k2 - 1

    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] -= arr[idx_k1]
        else:
            arr[i] -= arr[idx_k2]

    # б) Все элементы с нечетными номерами увеличить на 1,
    # с четными — уменьшить на 1
    for i in range(len(arr)):
        if (i + 1) % 2 == 1:
            arr[i] += 1
        else:
            arr[i] -= 1

# Вывод результата
print("Изменённый массив:", arr)
