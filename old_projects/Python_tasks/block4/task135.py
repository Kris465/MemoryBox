def traffic_light_color(t_minutes):

    t_seconds = t_minutes * 60

    cycle_length = 60

    time_in_cycle = t_seconds % cycle_length

    if 0 <= time_in_cycle < 30:
        return "Зелёный"
    elif 30 <= time_in_cycle < 35:
        return "Жёлтый"
    else:
        return "Красный"


t = float(input("Введите время в минутах, прошедшее с начала часа: "))

color = traffic_light_color(t)


print(f"Сигнал светофора: {color}")
