def count_consecutive_dry_days(rainfall):
    # Инициализируем счетчик дней без осадков
    count = 0
    # Проходим по каждому дню в мае
    for day in rainfall:
        if day == 0:
            # Если осадков не было, увеличиваем счетчик
            count += 1
        else:
            # Если осадки были, выходим из цикла
            break
    return count

# Тестовые случаи
# 1. В какие-то дни мая осадки выпадали
rainfall_case1 = [0, 0, 0, 5, 10, 15, 0, 0, 0]
print("Количество первых дней без осадков (случай 1):", count_consecutive_dry_days(rainfall_case1))

# 2. Осадков могло не быть ни в какой день мая
rainfall_case2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Количество первых дней без осадков (случай 2):", count_consecutive_dry_days(rainfall_case2))
