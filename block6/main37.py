def track_penalties():
    penalties = {'Команда 1': 0, 'Команда 2': 0}
    removals = {'Команда 1': 0, 'Команда 2': 0}
    
    while True:
        team = input("Введите номер команды (1/2) или 0 для завершения: ")
        if team == '0':
            break
            
        if team not in ('1', '2'):
            print("Неверный номер команды!")
            continue
            
        time = input("Введите время удаления (2, 5 или 10 минут): ")
        if time not in ('2', '5', '10'):
            print("Неверное время удаления!")
            continue
            
        team_key = f'Команда {team}'
        penalties[team_key] += int(time)
        removals[team_key] += 1
    
    print("\nИтоговая статистика:")
    for team in penalties:
        print(f"{team}: {removals[team]} удалений, {penalties[team]} минут штрафа")

# Запускаем программу
track_penalties()
