k = int(input("Введите номер дня: "))


if 1 <= k <= 365:
    day_of_week = (k - 1) % 7

    if day_of_week == 6 or day_of_week == 7:
        print(f'{k}-й день года - выходной.')
    else:
        print("Этот день рабочий. ")
else:
    print('Ошибка')
