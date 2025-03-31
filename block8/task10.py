scores = [[] for _ in range(5)]

for athlete in range(1, 9):
    print(f"Введите баллы для спортсмена {athlete} (5 баллов через пробел):")
    points = list(map(int, input().split()))
    for i in range(5):
        scores[i].append(points[i])

print("\nБаллы спортсменов по видам спорта:")
for sport in range(5):
    print(f"Вид спорта {sport + 1}: ", end="")
    for athlete in range(8):
        print(scores[sport][athlete], end=" ")
    print()

scores = []

for athlete in range(1, 9):
    print(f"Введите баллы для спортсмена {athlete} (5 баллов через пробел):")
    points = list(map(int, input().split()))
    scores.append(points)

print("\nБаллы спортсменов:")
for athlete in range(8):
    print(f"Спортсмен {athlete + 1}:\
        {scores[athlete][0]} {scores[athlete][1]}\
            {scores[athlete][2]} {scores[athlete][3]} {scores[athlete][4]}")
