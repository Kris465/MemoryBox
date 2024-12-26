football_players = [
    {"first_name": "Иван", "last_name": "Иванов", "goals": 2},
    {"first_name": "Петр", "last_name": "Петров", "goals": 0},
    {"first_name": "Сергей", "last_name": "Сергеев", "goals": 1},
    {"first_name": "Алексей", "last_name": "Алексеев", "goals": 3},
    {"first_name": "Дмитрий", "last_name": "Дмитриев", "goals": 0},
    {"first_name": "Максим", "last_name": "Максимов", "goals": 1},

]
players_with_goals = []

for player in football_players:
    if player["goals"] > 0:
       players_with_goals.append(player)

players_with_goals.sort(key=lambda x: (x['last_name'], x['first_name']))

print("Футболисты, которые забили хотя бы один гол: ")
for player in players_with_goals:
    print(f"{player['last_name']} {player['first_name']}")
