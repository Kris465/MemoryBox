month = int(input('Введите номер месяца (от 1 до 12):\n'))

season = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

found = False
for key, months in season.items():
    if month in months:
        print(f"Месяц относится к времени года: {key}")
        found = True
        break

if not found:
    print("Ошибка: введённое число не является номером месяца (1-12).")
