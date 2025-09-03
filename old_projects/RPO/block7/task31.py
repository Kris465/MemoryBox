n = int(input("Введите колличество комманд: "))
teams = []

for _ in range(n):
    wins, losses = map(int, input("Введите колличество побед\
        и поражений через пробел: ").split())
    teams.append((wins, losses))
better_teams = sum(wins > losses for wins, losses in teams)
print("Команда с большими победами: ", better_teams)
