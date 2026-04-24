# Ввод массива чисел через пробел
array = list(map(int, input("Введите числа через пробел: ").split()))

# Подсчет пар соседних элементов, где оба чётные
pair_count = 0
for i in range(len(array) - 1):
    if array[i] % 2 == 0 and array[i + 1] % 2 == 0:
        pair_count += 1

print("Количество пар соседних чётных элементов:", pair_count)
