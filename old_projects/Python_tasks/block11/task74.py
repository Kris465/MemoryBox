results = list(map(int, input("Введите результаты 20 игр (3 — победа, 2 — проигрыш, 1 — ничья): ").split()))

if len(results) != 20:
    print("Ошибка: необходимо ввести ровно 20 результатов.")
else:
    wins = sum(1 for r in results if r == 3)
    draws = sum(1 for r in results if r == 1)
    losses = sum(1 for r in results if r == 2)

    print("Количество побед:", wins)
    print("Количество ничьих:", draws)
    print("Количество поражений:", losses)
