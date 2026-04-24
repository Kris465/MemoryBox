from datetime import datetime, timedelta


def previous_day(m, n):
    return (datetime(2000, m, n) - timedelta(days=1)).strftime("%d.%m.")


def next_day(m, n):
    return (datetime(2000, m, n) - timedelta(days=1)).strftime("%d.%m.")


m = int(input("Введите номер месяца: "))
n = int(input("Введите число: "))


print(f'предыдущий день: {previous_day(m, n)}')
print(f'следующий день: {next_day(m, n)}')
