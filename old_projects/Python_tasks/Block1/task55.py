def time_to_meet(S, V1, V2):
    if V1 + V2 == 0:
        return None
    time = S / (V1 + V2)
    return time


S = int(input("Введите расстояние: "))
V1 = int(input("Введите скорость первого автомобиля: "))
V2 = int(input("Введите скорость второго автомобиля: "))

meeting_time = time_to_meet(S, V1, V2)
print(f"Время встречи автомобилей: {meeting_time} часов")
