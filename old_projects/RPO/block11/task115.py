speeds = [list(map(int, input("Введите массив: ").split()))]

max_speed = max(speeds)

first_index = speeds.index(max_speed) + 1

last_index = len(speeds) - 1 - speeds[::-1].index(max_speed) + 1

print("Порядковый номер первого самого быстрого автомобиля:", first_index)
print("Порядковый номер последнего самого быстрого автомобиля:", last_index)
