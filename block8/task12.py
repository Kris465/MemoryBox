sportsmen = []
for i in range(15):
    scores = list(map(int, input(f"Спортсмен {i+1}: ").split()))
    sportsmen.append(scores)

count_5 = sum(s.count(5) for s in sportsmen)
print(f"Общее количество пятерок: {count_5}")


print("Количество троек:")
for i in range(15):
    print(f"Спортсмен {i+1}: {sportsmen[i].count(3)}")


count_2 = [0] * 3
for s in sportsmen:
    for j in range(3):
        if s[j] == 2:
            count_2[j] += 1
print("Двоек по программам:")
for j in range(3):
    print(f"Программа {j+1}: {count_2[j]}")
