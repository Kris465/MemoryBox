temperatures = [64]

min_temp = None
count_cool_days = 0

for temp in temperatures:
    if min_temp is None or temp < min_temp:

        min_temp = temp
        count_cool_days = 1
    elif temp == min_temp:

        count_cool_days += 1

print(f"Самая прохладная температура: {min_temp}")
print(f"Количество прохладных дней: {count_cool_days}")
