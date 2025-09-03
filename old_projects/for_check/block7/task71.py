car_count = 25
average_speeds = []

for i in range(car_count):
    distance = float(input(f"Введите длину пути для автомобиля {i + 1} (в км): "))
    time = float(input(f"Введите время, затраченное автомобилем {i + 1} (в часах): "))
    average_speed = distance / time
    average_speeds.append(average_speed)

max_speed = max(average_speeds)
max_speed_index = average_speeds.index(max_speed) + 1

print(f"Порядковый номер автомобиля с максимальной средней скоростью: {max_speed_index}")
