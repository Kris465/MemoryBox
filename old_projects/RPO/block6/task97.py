def find_place(sorted_points, target_points):
    left, right = 0, len(sorted_points) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_points[mid] == target_points:
            return mid + 1
        elif sorted_points[mid] < target_points:
            right = mid - 1
        else:
            left = mid + 1

    return -1


sorted_points = [56, 54, 53, 50, 49, 48, 47, 45, 44, 43, 42, 40, 39, 38, 37,
                 36, 35, 34, 33, 32]
target_points = 47

place = find_place(sorted_points, target_points)
print(f"Команда, набравшая {target_points} очков, заняла {place} место.")
