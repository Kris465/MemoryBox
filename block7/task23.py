precipitation = [5, 10, 0, 8, 12, 7, 0, 9, 11, 6, 0, 10, 8, 12, 7, 0, 9, 11,
                 6, 0, 10, 8, 12, 7, 0, 9, 11, 6, 0, 10]

total_precipitation = sum(filter(lambda x: precipitation.index(x) % 2 == 0,
                                 precipitation))

print("Общее количество осадков за четные дни месяца:", total_precipitation)
