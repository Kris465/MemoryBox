
array = [/* ваши данные здесь */]


min_value = None
max_value = None
min_indices = []
max_indices = []

for i, value in enumerate(array):
    if min_value is None or value < min_value:
        min_value = value
        min_indices = [i]
    elif value == min_value:
        min_indices.append(i)
        
    if max_value is None or value > max_value:
        max_value = value
        max_indices = [i]
    elif value == max_value:
        max_indices.append(i)

print(f"Индексы элементов с минимальным значением ({min_value}): {min_indices}")
print(f"Индексы элементов с максимальным значением ({max_value}): {max_indices}")