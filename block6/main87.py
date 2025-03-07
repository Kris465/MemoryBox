def basketball_score():
    team1, team2 = 0, 0
    while True:
        points = int(input("Очки (1, 2, 3 или 0 для окончания): "))
        if points == 0:
            break
        team = input("Команда (1 или 2): ")
        if team == '1':
            team1 += points
        else:
            team2 += points
        print(f"Счет: {team1} - {team2}")
    if team1 > team2:
        print(f"Победила Команда 1: {team1} - {team2}")
    elif team2 > team1:
        print(f"Победила Команда 2: {team2} - {team1}")
    else:
        print(f"Ничья: {team1} - {team2}")

# Пример использования
basketball_score()
