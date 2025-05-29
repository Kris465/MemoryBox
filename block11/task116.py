precipitation = [list(map(int, input("Введите массив: ").split()))]

max_precip = max(precipitation)

first_day = precipitation.index(max_precip) + 1

last_day = len(precipitation) - 1 - precipitation[::-1].index(max_precip) + 1

print("Дата самого дождливого дня (первый случай):", first_day)
print("Дата самого дождливого дня (последний случай):", last_day)
