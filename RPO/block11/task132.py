arr = [3, 5, 2, 5, 1, 4, 5]

max_value = float('-inf')
second_max_value = float('-inf')
max_index = -1
second_max_index = -1

min_value = float('inf')
second_min_value = float('inf')
min_index = -1
second_min_index = -1

for i, val in enumerate(arr):

    if val > max_value:
        second_max_value = max_value
        second_max_index = max_index
        max_value = val
        max_index = i
    elif val > second_max_value and val != max_value:
        second_max_value = val
        second_max_index = i

    if val < min_value:
        second_min_value = min_value
        second_min_index = min_index
        min_value = val
        min_index = i
    elif val < second_min_value and val != min_value:
        second_min_value = val
        second_min_index = i

print("а) Максимальный элемент:", max_value)
print("Элемент без учета этого:", second_max_value)

print("б) Минимальный элемент:", min_value)
print("Элемент без учета этого:", second_min_value)

print("в) Номер максимального элемента (0-индекс):", max_index)
print("Номер второго по величине (без учета первого):", second_max_index)

print("г) Номер минимального элемента (0-индекс):", min_index)
print("Номер второго по минимальности (без учета первого):", second_min_index)
