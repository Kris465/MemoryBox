def count_results(points):
    wins = 0
    losses = 0
    draws = 0

    for point in points:
        if point == 3:
            wins += 1
        elif point == 0:
            losses += 1
        elif point == 1:
            draws += 1

    return wins, losses, draws


points_input = input("Введите очки, полученные командой за каждую игру: ")

points = []


current_number = ''
for char in points_input:
    if char == ',':
        if current_number != '':
            points.append(int(current_number))
            current_number = ''
    else:
        current_number += char


if current_number != '':
    points.append(int(current_number))

# Подсчет результатов
wins, losses, draws = count_results(points)


print(f"Количество выигрышей: {wins}")
print(f"Количество проигрышей: {losses}")
print(f"Количество ничьих: {draws}")
