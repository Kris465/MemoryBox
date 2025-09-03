precipitation = [0, 5, 0, 2, 0, 0, 3, 0, 4, 0, 1, 0,
                 0, 2, 0, 0, 3, 0, 1, 0, 4, 0, 2, 0,
                 0, 1, 0, 3, 0, 2, 0]

print("Дни месяца без осадков:")
for day in range(1, len(precipitation) + 1):
    if precipitation[day - 1] == 0:
        print(day)
