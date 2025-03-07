def calculate_time_from_angle(y):

    if not (0 <= y < 360):
        return "Угол y должен быть в диапазоне [0, 360)"
    

    hours = int(y // 30)
    

    remaining_angle = y - (hours * 30)
    

    minutes = int(remaining_angle // 0.5)
    
    return hours, minutes


y = 105.11
hours, minutes = calculate_time_from_angle(y)
print(f"Угол {y} градусов соответствует {hours} часам и {minutes} минутам.")
