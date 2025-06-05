temperatures = [list(map(int, input("Введите массив: ").split()))]

days_temperatures = list(enumerate(temperatures, start=1))

sorted_days = sorted(days_temperatures, key=lambda x: x[1])

coldest_day1, coldest_day2 = sorted_days[0][0], sorted_days[1][0]

print(f"Даты двух самых холодных \
    дней: {coldest_day1} и {coldest_day2} февраля")
