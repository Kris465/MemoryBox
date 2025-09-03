team1_score = 0
team2_score = 0

while True:
    points = int(input("Введите количество очков, заработанных\
 командой (1, 2, 3 или 0 для завершения): "))

    if points == 0:
        break

    elif points in [1, 2, 3]:
        team_number = input("Введите номер команды,\
 получившей очки (1 или 2): ")

        if team_number == '1':
            team1_score += points
        elif team_number == '2':
            team2_score += points

        print(f"Текущий счет:\
 Команда цска - {team1_score}, Команда спартак - {team2_score}")
    else:
        print("Неверное значение! Введите корректное количество очков.")

if team1_score > team2_score:
    winner = 'цска'
elif team2_score > team1_score:
    winner = 'спартак'
else:
    winner = 0

print("Игра окончена!")
if winner == 0:
    print("Итоговый счет: Ничья")
else:
    print(f"Победила команда {winner}!")
