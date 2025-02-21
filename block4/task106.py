while True:
    try:
        month = int(input('Введите число месяца (от 1 до 12):\n'))
        if 1 <= month <= 12:
            break
        else:
            print("Пожалуйста, введите число от 1 до 12.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

# Объединяем зимние месяцы в один список
seasons = {
    'зима': list(range(12, 13)) + list(range(1, 3)),
    'весна': range(3, 6),
    'лето': range(6, 9),
    'осень': range(9, 12)
}

# Определяем сезон
for season_name, months in seasons.items():
    if month in months:
        print(season_name)
