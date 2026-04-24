
prices = list(map(float, input("Введите цены товаров через пробел: ").split()))


expensive_total = 0

for price in prices:
    if price > 1000:
        expensive_total += price

print("Общая стоимость товаров дороже 1000 рублей:", expensive_total)
