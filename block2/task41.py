import math

def calculate_minute_angle_and_time(y):

    if not (0 < y <= 2 * math.pi):
        return "Угол y должен быть в диапазоне (0, 2π]"


    t_hours = (6 * y) / math.pi
    

    hours = int(t_hours)
    

    t_minutes = t_hours * 60
    

    minutes = int(t_minutes - (hours * 60))
    

    theta_m = 12 * y
    

    theta_m %= 2 * math.pi
    
    return theta_m, hours, minutes


y = math.pi / 6
theta_m, hours, minutes = calculate_minute_angle_and_time(y)
print(f"Угол минутной стрелки: {theta_m:.2f} радиан")
print(f"Количество полных часов: {hours}")
print(f"Количество полных минут: {minutes}")
