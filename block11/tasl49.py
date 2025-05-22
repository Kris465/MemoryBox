
arr = list(map(float, input("Введите массив вещественных \
    чисел через пробел: ").split()))


m1 = int(input("Введите номер m1 (начиная с 1): "))
m2 = int(input("Введите номер m2 (начиная с 1): "))


if not (1 <= m1 <= len(arr)) or not (1 <= m2 <= len(arr)):
    print("Номера m1 или m2 выходят за границы массива.")
else:
    idx_m1 = m1 - 1
    idx_m2 = m2 - 1

    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] += arr[idx_m1]
        else:
            arr[i] += arr[idx_m2]

    for i in range(len(arr)):
        if (i + 1) % 2 == 0:
            arr[i] *= 2
        else:
            arr[i] -= 1


print("Изменённый массив:", arr)
