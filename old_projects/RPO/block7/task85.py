
games = []

for i in range(20):
    game_result = input(f"Введите результат игры {i+1} в формате '0 1': ")
    try:
        scored_goals = int(game_result[0])
        conceded_goals = int(game_result[1])
        games.append((scored_goals, conceded_goals))
    except (IndexError, ValueError):
        print("Неверный формат ввода. Повторите попытку.")
        continue

for game in games:
    if game[0] > game[1]:
        result = "выигрыш"
    elif game[0] == game[1]:
        result = "ничья"
    else:
        result = "проигрыш"
    print(f"Игра: {game}, Результат: {result}")

wins = sum(1 for game in games if game[0] > game[1])
print(f"Количество выигрышей: {wins}")

losses = sum(1 for game in games if game[0] < game[1])
print(f"Количество выигрышей: {wins}, Количество проигрышей: {losses}")

draws = sum(1 for game in games if game[0] == game[1])
print(f"Количество выигрышей: {wins}, Количество ничьих: {draws},\
    Количество проигрышей: {losses}")

big_difference_games = sum(1 for game in games if abs(game[0] - game[1]) >= 3)
print(f"Количество игр с разницей забитых и пропущенных мячей >= 3:\
    {big_difference_games}")
