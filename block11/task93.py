
prices = [120, 85, 150, 90, 200, 75, 130, 110, 95, 180,
          140, 160, 105, 115, 125, 135, 145, 155, 165, 175]


total_price = sum(prices)


average_price = total_price / len(prices)


count_below_average = sum(1 for price in prices if price < average_price)

print(f"Количество видов товара с ценой меньше средней: {count_below_average}")
