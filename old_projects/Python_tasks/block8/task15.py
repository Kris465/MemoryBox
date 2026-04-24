scores = [[] for _ in range(5)]

for athlete in range(1, 9):
    print(f"Введите баллы для спортсмена {athlete} (5 баллов через пробел):")
    points = list(map(int, input().split()))
    for i in range(5):
        scores[i].append(points[i])

a = max(points)
print("Максимально набрали : ", a, "Баллов")

total_scores = [s for s in points]

winner_index = total_scores.index(max(total_scores)) + 1

print(f"Победил спортсмен №{winner_index},\
      набравший {max(total_scores)} баллов.")
