heights = [
    180, 175, 190, 185, 178, 180, 190, 175, 180, 185,
    180, 178, 185, 190, 180, 185, 180, 175, 190, 180,
    185, 180, 178, 185, 190, 180, 185, 180, 175, 190,
    180, 185, 180, 178, 185
]


max_height = max(heights)


count_max_height = heights.count(max_height)

print(f'Количество людей с \
    наибольшим ростом ({max_height} см): {count_max_height}')
