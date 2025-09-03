arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]

min_value = min(arr)
min_index = arr.index(min_value)

max_value = max(arr)
max_index = arr.index(max_value)

if min_index < max_index:
    print("Минимальное число встречается раньше.")
elif max_index < min_index:
    print("Максимальное число встречается раньше.")
else:
    print("Минимальное и максимальное числа встречаются одновременно.")
