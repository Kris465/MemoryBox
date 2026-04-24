array = [10, 15, 20, 25, 30, 18, 22]

average_value = sum(array) / len(array)

closest_element = array[0]
min_diff = abs(array[0] - average_value)

for element in array:
    diff = abs(element - average_value)
    if diff < min_diff:
        min_diff = diff
        closest_element = element

print(f"Элемент, наиболее близкий к среднему ({average_value:.2f}) : \
    {closest_element}")
