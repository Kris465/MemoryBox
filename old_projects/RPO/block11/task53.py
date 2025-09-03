arr = list(map(int, input("Введите массив целых чисел через пробел: ").split()))

m = int(input("Введите число m: "))
n = int(input("Введите число n: "))

for i in range(len(arr)):
    if arr[i] % 10 == 0:
        arr[i] = 0

for i in range(len(arr)):
    if arr[i] % 2 != 0:
        arr[i] *= 2
    else:
        arr[i] //= 2

for i in range(len(arr)):
    if arr[i] % 2 != 0:
        arr[i] -= m

for i in range(0, len(arr), 2):
    arr[i] += n

print("Изменённый массив:", arr)
