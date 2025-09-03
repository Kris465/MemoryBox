team_a_penalties = []
team_b_penalties = []

while True:
    try:
        input_time = int(input("Введите штрафное время (в минутах): "))
        if input_time == 0:
            break

        team = input("Введите команду (A/B): ").upper()
        minutes = int(input("Введите длительность штрафа (2/5/10 минут): "))

        if team == 'A':
            team_a_penalties.append(minutes)
        elif team == 'B':
            team_b_penalties.append(minutes)
        else:
            print("Некорректная команда! Попробуйте снова.")

    except ValueError:
        print("Ошибка ввода! Пожалуйста, введите корректное значение.")

total_team_a = sum(team_a_penalties)
total_team_b = sum(team_b_penalties)

print(f"Общее штрафное время команды A: {total_team_a} минут")
print(f"Общее штрафное время команды B: {total_team_b} минут")
