month = int(input("Введите номер месяца (1 - 12): "))
day = int(input("Введите номер дня (1 до числа в месяце): "))

days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def previous_day(month, day):
    if day > 1:
        return month, day - 1
    else:
        if month > 1:
            month -= 1
            return month, days_in_month[month]
        else:
            print("Некорректная дата")
            return None


def next_day(month, day):
    if day < days_in_month[month]:
        return month, day + 1
    else:
        if month < 12:
            month += 1 
            return month, 1
        else:
            print("Некорректная дата.")
            return None
        

prev_date = previous_day(month, day)
next_date = next_day(month, day)


if prev_date is not None:
    print(f'Предыдущий день {prev_date[1]}.{prev_date[0]}')
if next_day is not None: 
    print(f'Следующий день {next_date[1]}.{next_date[0]}')
