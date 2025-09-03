precipitations = [10, 20, 15, 20, 5, 20, 12, 20, 8, 20, 7, 20, 9, 20, 11, 20,
                  13, 20, 14, 20, 16, 20, 17, 20, 18, 20, 19, 20, 21, 20, 22]
max_precipitation = max(precipitations)
count_max_days = precipitations.count(max_precipitation)
print("Количество дней с максимальным количеством осадков:", count_max_days)
