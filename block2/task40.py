def time_from_angle(y):
    hours = y / 30
    full_hours = int(hours)
    minutes = (hours - full_hours) * 60
    return full_hours, round(minutes)


y = float(input("Укажите угол поворота часовой стрелки (градусы): "))
full_hours, minutes = time_from_angle(y)
print(f"Прошли {full_hours} часов и {minutes} минут.")
