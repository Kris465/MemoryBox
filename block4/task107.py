def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def get_days_in_month(month, leap_year = False):
    if month == 2 and leap_year:
        return 29
    elif month in (4, 6,  9, 11):
        return 30
    else:
        return 31
    
month = int(input("Введите номер месяц (от 1 до 12): "))
leap_year = input("Введите год (или нажмите Enter, если год невисокосный)")

if leap_year:
    leap_year = is_leap_year(int(leap_year))
else:
    leap_year = False

days = get_days_in_month(month, leap_year)
print(f"В этом месяце {days} дней.")
