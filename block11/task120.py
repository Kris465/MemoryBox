# Предположим, у нас есть массив с ростами
heights = [170, 180, 165, 180, 172, 180, ...]  # всего 35 элементов


max_height = max(heights)

# Подсчитываем количество человек с этим ростом
count_max = heights.count(max_height)

print(f"Самый большой рост: {max_height}")
print(f"Количество человек с этим ростом: {count_max}")
