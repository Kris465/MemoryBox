array = list(map(int, input("Введите числа через пробел: ").split()))

pair_count = 0
for i in range(len(array) - 1):
    if array[i] % 10 == 0 and array[i + 1] % 10 == 0:
        pair_count += 1

print("Количество пар соседних элементов, оканчивающихся нулём:", pair_count)
