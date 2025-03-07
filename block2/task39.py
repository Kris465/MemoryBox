def calculate_hour_angle(h, m, s):

    if not (0 < h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        return "Некорректные входные данные"
    

    angle_hours = h * 30
    

    angle_minutes = m * 0.5
    

    angle_seconds = s * (0.5 / 60)
    

    total_angle = angle_hours + angle_minutes + angle_seconds
    

    total_angle %= 360
    
    return total_angle


h = 3
m = 30
s = 45
angle = calculate_hour_angle(h, m, s)
print(f"Угол между положением часовой стрелки в начале суток и {h}:{m}:{s} = {angle:.2f} градусов")
