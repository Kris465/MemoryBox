import random
costs = [random.randint(100, 1000) for _ in range(60)]


min_cost = min(costs)


count_cheapest = costs.count(min_cost)


print(f"Минимальная стоимость книги: {min_cost}")
print(f"Количество самых дешевых книг: {count_cheapest}")
