a = [list(map(int, input("Введите массив: ").split()))]

sorted_a = sorted(a, key=lambda x: x[0])

best_team = sorted_a[:4]

i, j, k, m = [idx for (val, idx) in best_team]

i, j, k, m = sorted([i, j, k, m])

print(f"Лучшая команда: {i}, {j}, {k}, {m}")
print(f"Сумма их результатов: {sum(val for val, idx in best_team)}")
