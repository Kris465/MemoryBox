flowers = 2
summa = 2
days = int(input("Сколько дней Лунтик собирает цветы? "))
for day in range(1, days):
    flowers = flowers + 1
    summa += flowers

print(f"Лунтик собрал {summa} цветов за {days} дней.")
