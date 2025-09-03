def bisect_insert(heights, new_height):
    left, right = 0, len(heights)
    while left < right:
        mid = (left + right) // 2
        if heights[mid] > new_height:
            left = mid + 1
        else:
            right = mid
    heights.insert(left, new_height)


def insert_by_values_efficient(heights, new_height1, new_height2):
    if new_height1 > new_height2:
        bisect_insert(heights, new_height1)
        bisect_insert(heights, new_height2)
    else:
        bisect_insert(heights, new_height2)
        bisect_insert(heights, new_height1)
    return heights


heights = [180, 175, 170, 165, 160]
new_height1, new_height2 = 172, 168
updated_heights = insert_by_values_efficient(heights, new_height1, new_height2)
print(updated_heights)
