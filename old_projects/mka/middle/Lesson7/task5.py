carrots = 1
summa = 1
days = int(input("Сколько дней Крош собирал морковки? "))
for day in range(1, days):
    carrots = carrots + 2
    summa += carrots

print(f"Крош собрал {summa} морковок за {days} дней!")
