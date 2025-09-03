initial_amount = int(input("Начальные деньги: "))
monthly_increase_rate = float(input("Коэффициент: "))
current_amount = initial_amount
month = 0

while True:
    month += 1
    increase = current_amount * monthly_increase_rate
    current_amount += increase

    if increase > 30:
        print(f"Ежемесячное увеличение превысит 30 руб. на {month}-й месяц.")
        break

current_amount = initial_amount
month = 0


while current_amount <= 1200:
    month += 1
    increase = current_amount * monthly_increase_rate
    current_amount += increase

print(f"Вклад превысит 1200 руб. через {month} месяцев.")
