initial_deposit = 1000
monthly_interest_rate = 0.02
current_amount = initial_deposit
growth = []


for month in range(1, 11):
    interest = current_amount * monthly_interest_rate
    growth.append(interest)
    current_amount += interest


print("Прирост суммы вклада за первые 10 месяцев:")
for month in range(10):
    print(f"Месяц {month + 1}: {growth[month]:.2f} руб.")


current_amount = initial_deposit


print("\nСумма вклада через 3, 4,..., 12 месяцев:")
for month in range(1, 13):
    interest = current_amount * monthly_interest_rate
    current_amount += interest
    if month >= 3:
        print(f"Месяц {month}: {current_amount:.2f} руб.")
