prices = [12.99, 8.50, 15.00, 8.50, 20.00, ...]

min_price = None
count_min = 0

for price in prices:
    if min_price is None or price < min_price:
        min_price = price
        count_min = 1
    elif price == min_price:
        count_min += 1

print(f"Самая низкая цена: {min_price}")
print(f"Количество самых дешевых книг: {count_min}")
