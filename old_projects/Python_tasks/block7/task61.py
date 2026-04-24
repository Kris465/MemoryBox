results = list(map(float, input("\
    Введите результаты спортсменов через пробел: ").split()))
best_time = max(results)
best_index = results.index(best_time)
print("Лыжник с лучшим результатом стартовал под номером:", best_index + 1)
