
precipitations = [10, 20, 15, 20, 25, 25, 18, ...]


max_precipitation = None
count_max_days = 0

for precipitation in precipitations:
    if max_precipitation is None or precipitation > max_precipitation:

        max_precipitation = precipitation
        count_max_days = 1
    elif precipitation == max_precipitation:

        count_max_days += 1

print(f"Максимальное количество осадков за месяц: {max_precipitation}")
print(f"Количество дней с этим количеством осадков: {count_max_days}")
