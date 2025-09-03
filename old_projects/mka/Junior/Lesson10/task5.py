toys = {
    "Микки Маус": 10,
    "Супермен": 15,
    "Барби": 12,
}

cart = []
total_cost = 0

while True:
    toy = input("Введите имя игрушки для добавления в корзину (или 'стоп' для завершения): ")
    if toy.lower() == 'стоп':
        break
    if toy in toys:
        cart.append(toy)
        total_cost += toys[toy]
    else:
        print("Эта игрушка недоступна.")

print(f"Вы купили: {cart}. Общая стоимость: {total_cost} долларов.")
