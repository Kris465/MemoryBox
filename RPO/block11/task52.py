
arr = list(map(int, input("Введите массив целых \
    чисел через пробел: ").split()))


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))


for i in range(len(arr)):
    if abs(arr[i]) % 10 == 4:
        arr[i] //= 2


for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] = arr[i] ** 2
    else:
        arr[i] *= 2


for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] += a


for i in range(1, len(arr), 2):
    arr[i] -= b


print("Изменённый массив:", arr)
