def find_lowest_team(points):
    min_point = min(points)
    return points.index(min_point) + 1


points = [10, 15, 8, 12, 8]
team = find_lowest_team(points)
print(f"Команда с наименьшим количеством очков: №{team}")
