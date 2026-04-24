
speeds = [list(map(int, input("Введите массив: ").split()))]


max_speed = float('-inf')
second_max_speed = float('-inf')

for speed in speeds:
    if speed > max_speed:
        second_max_speed = max_speed
        max_speed = speed
    elif speed > second_max_speed and speed != max_speed:
        second_max_speed = speed

print("Две самые быстрые скорости:", max_speed, second_max_speed)
