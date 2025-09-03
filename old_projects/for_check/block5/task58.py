def sport_score(results):
    if results[0] > results[1]:
        return 'Первое место'
    elif results[0] == results[1]:
        return 'Ничья'
    else:
        return 'Второе место'


results = [20, 18]
print("Результаты соревнований:", sport_score(results))
