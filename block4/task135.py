def traffic_light_color(t):
    time_in_cycle = t % 6

    if 0 <= time_in_cycle <3:
        return "Зеленый"
    elif 3 <= time_in_cycle < 4:
        return"Желтый"
    else:
        return "Красный"
    

t = float(input("Введите время в минутах, прошедшее с начала часа: "))
color = traffic_light_color(t)
print(f"Сигнал светофора: {color}")
