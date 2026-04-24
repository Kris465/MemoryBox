arr = list(range(1, 21))


new_arr = arr[-3:] + arr[3:-3] + arr[:3]

print("Исходный массив:", arr)
print("После перестановки:", new_arr)
