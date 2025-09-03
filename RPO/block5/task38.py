def strange_husband(n):
    # Начальное расстояние от дома
    distance_from_home = 0.0
    
    # Общий путь, который прошел мужчина
    total_distance_traveled = 0.0
    
    for i in range(1, n + 1):
        # Расстояние, которое мужчина проходит на текущем этапе
        step_distance = 1 / (2 ** i)
        
        # Направление движения меняется на противоположное каждые два шага
        if i % 2 == 1:
            distance_from_home += step_distance
        else:
            distance_from_home -= step_distance
            
        # Обновляем общий путь
        total_distance_traveled += step_distance
    
    return distance_from_home, total_distance_traveled

# Рассчитаем результаты для 100-го этапа
distance_after_100_steps, total_distance_traveled = strange_husband(100)
print(f'Расстояние от дома после 100-го этапа: {distance_after_100_steps:.6f} км')
print(f'Общий путь, пройденный мужем: {total_distance_traveled:.6f} км')