array = list(map(int, input("Введите числа через пробел: ").split()))

count = 0
for i in range(1, len(array) - 1):
    if array[i] > array[i - 1] and array[i] > array[i + 1]:
        count += 1

print("Количество элементов, больших своих соседей:", count)
