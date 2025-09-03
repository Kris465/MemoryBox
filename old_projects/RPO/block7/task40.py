teams = {
    1: {'count': 0, 'time': 0},
    2: {'count': 0, 'time': 0}
}


n = 24


for i in range(n):
    team_number = int(input(f"Введите номер команды (1 или 2) для удаления {i + 1}: "))
    penalty_time = int(input("Введите время удаления (2, 5 или 10 минут): "))


    if team_number in teams:
        teams[team_number]['count'] += 1
        teams[team_number]['time'] += penalty_time
    else:
        print("Некорректный номер команды. Пожалуйста, введите 1 или 2.")


for team, data in teams.items():
    print(f"Команда {team}:")
    print(f" - Общее число удалений: {data['count']}")
    print(f" - Общее время удалений: {data['time']} минут")
