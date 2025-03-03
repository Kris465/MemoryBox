import math
from math import radians


def calculate_time_and_angles(angle_y):
    # Конвертируем угол в градусы
    degrees = math.degrees(angle_y)

    # Определяем количество полных оборотов часовой стрелки
    hours_full = int(degrees / 30)

    # Определяем минуты
    minutes_total = (degrees - hours_full * 30) * 2
    minutes_full = int(minutes_total)

    # Определяем угол минутной стрелки
    minute_angle = minutes_full * 6

    return hours_full, minutes_full, minute_angle


angle_in_radians = radians(135)
hours, minutes, minute_angle = calculate_time_and_angles(angle_in_radians)

print(f"Прошли {hours} часов и {minutes} минут.")
print(f"Угол минутной стрелки: {minute_angle} градусов.")
