import datetime


g = 2023
m = 3
n = 7


d = datetime.date(g, m, n)


one_day = datetime.timedelta(days=1)


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


prev_day = d - one_day


next_day = d + one_day


print(f"Дата: {d}")
print(f"Дата предидущего дня: {prev_day}")
print(f"Дата следующего дня: {next_day}")


if is_leap_year(g):
    print("Заданный год является високосным.")
else:
    print("заданный год не является високосным.")
