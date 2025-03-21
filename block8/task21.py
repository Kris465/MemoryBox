num_days = 10
num_stores = 3

income = []

for store in range(num_stores):
    print(f"Введите доход для магазина {store + 1} за {num_days} \
        дней через пробел:")
    daily_income = list(map(float, input().split()))
    income.append(daily_income)

max_income_days = []
for store_income in income:
    max_income_day = store_income.index(max(store_income)) + 1
    max_income_days.append(max_income_day)

print("\nДни, когда каждый магазин получил максимальный доход:")
for i in range(num_stores):
    print(f"Магазин {i + 1}: День {max_income_days[i]}")

max_income_per_day = []
for day in range(num_days):
    max_store_index = max(range(num_stores), key=lambda x: income[x][day])
    max_income_per_day.append(max_store_index + 1)

print("\nМагазины с максимальным доходом за каждый день:")
for day in range(num_days):
    print(f"День {day + 1}: Магазин {max_income_per_day[day]}")
