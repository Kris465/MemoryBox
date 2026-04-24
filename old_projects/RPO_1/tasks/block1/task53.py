price_monitor = 12000
price_pc = 40000
price_keyboard = 5000
price_mouse = 3000
total_price = price_monitor + price_pc + price_keyboard + price_mouse

count = int(input("Введите количество компьютеров: "))
print("Цена 3х компьютеров:", total_price)
print(f"Цена {count} компьютеров: {total_price * count}")
