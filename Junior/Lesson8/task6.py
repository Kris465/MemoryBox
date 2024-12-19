def add_hero(team):
    name = input("Введите имя супергероя: ")
    power = input("Введите силу супергероя: ")

    team[name] = power
    return team


team = {}
team = add_hero(team)
print(team)
