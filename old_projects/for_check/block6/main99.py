# Начальный пробег
distance_day = 10  # км

# Процент увеличения
increase_percent = 0.1

# Инициализация счетчика дней
day = 1

# Поиск дня, когда пробег превысит 20 км
while distance_day <= 20:
    distance_day *= (1 + increase_percent)
    day += 1

print(f"День, когда пробег превысит 20 км: {day}")

# Сброс переменных для поиска суммарного пробега
distance_day = 10
total_distance = 0
day = 1

# Поиск дня, когда суммарный пробег превысит 100 км
while total_distance <= 100:
    total_distance += distance_day
    distance_day *= (1 + increase_percent)
    day += 1

print(f"День, когда суммарный пробег превысит 100 км: {day}")
