def insert_numbers(heights, num1, num2):
    if not heights:
        return [num2, num1]

    heights.insert(0, num2)

    index = 1
    heights.insert(index + 1, num1)

    return heights


heights = [185, 180, 175, 170, 165]
num1 = 177
num2 = 190
updated_heights = insert_numbers(heights, num1, num2)
print(updated_heights)
