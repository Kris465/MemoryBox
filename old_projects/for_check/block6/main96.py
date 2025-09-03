def find_position(sorted_heights, new_height):
    left, right = 0, len(sorted_heights) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_heights[mid] < new_height:
            right = mid - 1
        else:
            left = mid + 1
    
    return left + 1  # +1, так как индексация начинается с 0

# Пример использования
sorted_heights = [190, 185, 180, 175, 170, 165, 160, 155, 150, 145, 140, 135, 130, 125, 120]
new_height = 172

position = find_position(sorted_heights, new_height)
print(f"Рост нового ученика займет {position} место в перечне.")
