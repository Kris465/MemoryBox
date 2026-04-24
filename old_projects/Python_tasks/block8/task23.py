price_per_item = []
quantity_sold = []
for product_id in range(1, 6):
    price = float(input(f"Введите стоимость товара {product_id}: "))
    price_per_item.append(price)

for day in range(1, 7):
    print(f"Введите количество проданных товаров за день {day} \
        для каждого вида товара через пробел:")
    row = list(map(int, input().split()))
    quantity_sold.append(row)

if len(quantity_sold) != 6 or any(len(day_quantity) != 5 for day_quantity
                                  in quantity_sold):
    print("Ошибка: введены некорректные данные!")
else:
    revenue_per_product = []
    for product_id in range(5):
        total_revenue = sum(quantity_sold[day][product_id] *
                            price_per_item[product_id] for day in range(6))
        revenue_per_product.append(total_revenue)
        print(f"Доход от продажи \
              товара {product_id + 1}: {total_revenue:.2f} руб.")

    daily_revenues = []
    for day in range(6):
        daily_revenue = sum(quantity_sold[day][product_id] *
                            price_per_item[product_id] for
                            product_id in range(5))
        daily_revenues.append(daily_revenue)
        print(f"Доход за день {day + 1}: {daily_revenue:.2f} руб.")

    total_revenue = sum(revenue_per_product)
    print(f"Общий доход магазина за 6 дней: {total_revenue:.2f} руб.")

    max_revenue_product = revenue_per_product.index(
        max(revenue_per_product)) + 1
    print(f"Максимальный доход получен от товара {max_revenue_product}.")

    max_daily_revenue_day = daily_revenues.index(max(daily_revenues)) + 1
    print(f"Максимальный доход за день \
          получен в день {max_daily_revenue_day}.")

    a = int(input("Введите порог дохода (a): "))
    days_above_threshold = sum(1 for revenue in daily_revenues if revenue > a)
    print(f"Количество дней, когда доход \
          превысил {a} руб.: {days_above_threshold}.")
