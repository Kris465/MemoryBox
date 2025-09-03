def total_expensive_cost(prices):
    return sum(price for price in prices if price > 1000)


n = int(input("Введите количество товаров: "))
prices = [int(input(f"Введите цену товара {i+1}:")) for i in range(n)]

result = total_expensive_cost(prices)
print(f"общая стоимость дорогих товаров, {result}")
