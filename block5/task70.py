def amoeba_cells(hours):
    cells = 1
    for hour in range(3, hours + 1, 3):
        cells *= 2
    return cells


hours = [3, 6, 9, 12, 15, 18, 21, 24]
results = [amoeba_cells(hour) for hour in hours]
for hour, result in zip(hours, results):
    print("Через {} часов: {} клеток".format(hour, result))
