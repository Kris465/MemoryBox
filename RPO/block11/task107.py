array = [4, 7, 2, 9, 5, 9, 1, 3]

max_element = max(array)

min_element = min(array)

difference = max_element - min_element

index_max = array.index(max_element)

index_min = array.index(min_element)

print("Максимальный элемент:", max_element)
print("Минимальный элемент:", min_element)
print("Разница между максимумом и минимумом:", difference)
print("Индекс максимального элемента:", index_max)
print("Индекс минимального элемента:", index_min)
