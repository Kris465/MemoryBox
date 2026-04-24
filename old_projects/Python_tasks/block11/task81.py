precipitations = list(map(int, input("Введите количество осадков за каждый день марта (всего 31 день): ").split()))

if len(precipitations) != 31:
    print("Ошибка: необходимо ввести ровно 31 значение.")
else:
    no_precip_days = sum(1 for p in precipitations if p == 0)

    if no_precip_days == 10:
        print("Верно: в месяце было ровно 10 дней без осадков.")
    else:
        print("Неверно: количество дней без осадков не равно 10.")
