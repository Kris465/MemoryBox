# Ввод количества осадков за каждый день августа через пробел
precipitations = list(map(float, input("Введите количество осадков за каждый \
                            день августа (31 день) через пробел: ").split()))

# Проверка правильности ввода
if len(precipitations) != 31:
    print("Ошибка: необходимо ввести ровно 31 значение.")
else:
    # Отбираем дни с дождем (осадки > 0)
    rainy_days = [p for p in precipitations if p > 0]

    # Проверяем, есть ли такие дни
    if len(rainy_days) == 0:
        print("В августе не было дней с дождем.")
    else:
        # Вычисляем среднее количество осадков в дождливые дни
        average_precipitation = sum(rainy_days) / len(rainy_days)
        print("Среднее количество осадков в дождливые дни:",
              average_precipitation)
