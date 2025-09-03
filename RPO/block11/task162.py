def insert_by_position(heights, new_height, position):
    heights.insert(position, new_height)
    heights.sort(reverse=True)
    return heights


heights = [list(map(int, input("Введите массив: ").split()))]
new_height = int(input("Введите рост нового ученика"))
position = int(input("Введите позицию нового ученика"))
updated_heights = insert_by_position(heights, new_height, position)
print(updated_heights)


def insert_by_height(heights, new_height):
    index = 0
    while index < len(heights) and heights[index] > new_height:
        index += 1
    heights.insert(index, new_height)
    return heights


heights = [list(map(int, input("Введите массив: ").split()))]
new_height = int(input("Введите рост нового ученика"))
updated_heights = insert_by_height(heights, new_height)
print(updated_heights)
