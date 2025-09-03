def calculate_hour_hand_angle(h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    angle_per_second = 360 / 43200
    angle = total_seconds * angle_per_second
    return angle


h = 3
m = 27
s = 36

angle = calculate_hour_hand_angle(h, m, s)
print(f"Угол между часовой стрелкой и началом суток: {angle:.2f} градусов")
