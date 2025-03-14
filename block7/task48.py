def calculate_avg_height(heights):
    boys_heights = []
    girls_heights = []
    for height in heights:
        if height < 0:
            boys_heights.append(-height)
        elif height > 0:
            girls_heights.append(height)

    avg_boys_height = sum(boys_heights) / len(boys_heights)\
        if boys_heights else 0
    avg_girls_height = sum(girls_heights) / len(girls_heights)\
        if girls_heights else 0

    return avg_boys_height, avg_girls_height


heights = [-170, 160, -180, 150, -175, 165]
avg_boys_height, avg_girls_height = calculate_avg_height(heights)

print(f"Средний рост мальчиков: {avg_boys_height:.2f}")
print(f"Средний рост девочек: {avg_girls_height:.2f}")
