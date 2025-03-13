# Данные о количестве осадков за каждый день месяца
precipitation = [5, 10, 0, 8, 12, 7, 0, 9, 11, 6, 0, 10, 8, 12, 7, 0, 9, 11,
                 6, 0, 10, 8, 12, 7, 0, 9, 11, 6, 0, 10]

# Подсчет осадков за четные дни (второй, четвертый и т.д.)
total_precipitation = sum(precipitation[i] for i in range(1, len(precipitation
                                                                 ), 2))
print("Общее количество осадков за четные дни месяца:", total_precipitation)
