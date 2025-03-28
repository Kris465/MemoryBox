speeds = []

for i in range(20):
    speed = float(input(f"Введите максимальную скорость для\
                        автомобиля {i + 1}: "))
    speeds.append(speed)

max_speed = max(speeds)

print(f"Максимальная скорость самого быстрого автомобиля: {max_speed} км/ч")
