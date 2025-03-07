from random import randint


def find_position(heights, new_height):
    low, high = 0, len(heights) - 1

    while low <= high:
        mid = (low + high) // 2
        if heights[mid] < new_height:
            high = mid - 1
        elif heights[mid] > new_height:
            low = mid + 1
        else:
            return mid + 1

    return low + 1


heights = [randint(0, 175) for i in range(15)]
new_height = 175
position = find_position(heights, new_height)
print(position)
