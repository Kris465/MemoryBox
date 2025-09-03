
wind_directions = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 2, 4, ...]


counts = {i:0 for i in range(1,9)}


for direction in wind_directions:
    if direction in counts:
        counts[direction] += 1


min_days = min(counts.values())
least_common_directions = [dir for dir, count in
                           counts.items() if count == min_days]


direction_names = {
    1: "северный",
    2: "южный",
    3: "восточный",
    4: "западный",
    5: "северо-западный",
    6: "северо-восточный",
    7: "юго-западный",
    8: "юго-восточный"
}

print("Наименее частое направление ветра(я):")
for dir_code in least_common_directions:
    print(f"{direction_names[dir_code]} ({counts[dir_code]} дней)")
