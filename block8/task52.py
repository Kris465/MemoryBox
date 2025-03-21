for bulls in range(0, 101):
    for cows in range(0, 101 - bulls):
        calves = 100 - bulls - cows
        if calves < 0:
            continue
        if bulls * 10 + cows * 5 + calves * 0.5 == 100:
            print(f"Быки: {bulls}, Коровы: {cows}, Телята: {calves}")
