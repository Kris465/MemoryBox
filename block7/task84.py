games = []


for i in range(20):
    goals_scored = int(input(f"Введите количество забитых мячей в игре\
        {i+1}: "))
    goals_conceded = int(input(f"Введите количество пропущенных мячей в игре \
        {i+1}: "))
    games.append((goals_scored, goals_conceded))


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
