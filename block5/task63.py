areas = [500, 600, 700, 800, 900, 400, 300, 200, 150, 250]
yields = [40, 45, 50, 55, 60, 42, 38, 36, 34, 39]

total_wheat = sum(a * y for a, y in zip(areas, yields))
average_yield = total_wheat / sum(areas)

print(f"Общее кол-во пшеницы, собрание в области: {total_wheat} центнеров.")
print(f"Средняя урожайность по области: {average_yield} центнеров с гектара")
