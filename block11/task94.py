precipitations = [12, 5, 0, 20, 15, 8, 10, 0, 7, 14,
                  9, 11, 13, 6, 4, 16, 18, 3, 2, 19,
                  21, 17, 22, 23, 24, 25, 26, 27, 28, 29,
                  30]


total_precipitation = sum(precipitations)


average_precipitation = total_precipitation / len(precipitations)


days_above_average = [day + 1 for day, precip in enumerate(precipitations)
                      if precip > average_precipitation]


print("Дни с осадками больше среднего:")
for day in days_above_average:
    print(f"День {day}")
