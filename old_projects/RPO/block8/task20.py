income = [
    [1000, 1200, 1100, 1300, 1400, 1500, 1600, 1700, 1800, 1900],
    [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900],
    [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900]
]


best_shop = max(range(len(income)), key=lambda i: sum(income[i])) + 1


daily_totals = [sum(day) for day in zip(*income)]
best_day = daily_totals.index(max(daily_totals)) + 1

max_income = max(max(day) for day in zip(*income))


for i, shop in enumerate(income):
    if max_income in shop:
        best_shop_for_max = i + 1
        best_day_for_max = shop.index(max_income) + 1
        break

print("а) Лучший магазин:", best_shop)
print("б) Лучший день:", best_day)
print("в) Магазин и день с макс. доходом:", best_shop_for_max, "магазин,", )
