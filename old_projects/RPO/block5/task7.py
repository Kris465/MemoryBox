price_per_item = 20.4

print("Количество товара | Стоимость")
print("-" * 30)

for quantity in range(2, 21):
    total_cost = price_per_item * quantity
    print(f"{quantity:>15} | {total_cost:>10.2f}")
