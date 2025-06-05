
prices = [list(map(int, input("Введите массив: ").split()))]


max_price = float('-inf')
second_max_price = float('-inf')

for price in prices:
    if price > max_price:
        second_max_price = max_price
        max_price = price
    elif price > second_max_price and price != max_price:
        second_max_price = price

print("Две самые дорогие стоимости:", max_price, second_max_price)
