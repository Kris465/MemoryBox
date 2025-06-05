
array = [list(map(int, input("Введите массив: ").split()))]

distinct_count = len(set(array))

print(f"Количество различных чисел в массиве: {distinct_count}")
