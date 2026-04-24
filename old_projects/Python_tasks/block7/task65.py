def height_diff(heights):
    return max(heights) - min(heights)


heights = [170, 160, 180, 175, 165]
diff = height_diff(heights)
print(f"Разница в росте: {diff} см")
