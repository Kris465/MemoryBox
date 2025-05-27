
precipitations = [
    700, 650, 720, 680, 710, 690, 730, 640, 660, 700,
    710, 680, 690, 720, 700, 710, 680, 690, 720, 700,
    710, 680, 690, 720, 700, 710, 680, 690, 720, 700,
    710, 680, 690, 720, 700, 710, 680, 690, 720, 700,

]


average_precipitation = sum(precipitations) / len(precipitations)


for year_index in range(len(precipitations)):
    year_number = year_index + 1
    deviation = precipitations[year_index] - average_precipitation
    print(f"Год {year_number}: Осадки = {precipitations[year_index]} мм,"
          f" отклонение от среднего = {deviation:.2f} мм")
