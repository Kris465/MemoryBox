from datetime import datetime, timedelta


def previous_day(m, n):
    return (datetime(2000, m, n) - timedelta(days=1)).strftime("%d.%m.")

def next_day(m, n):
    return (datetime(2000, m, n) + timedelta(days=1)).strftime("%d.%m.")


m = int(input("Введите номер месяца: "))
n = int(input("Введите число: "))


print(f"Предыдущий день: {previous_day(m, n)}")
print(f"Следующий день: {next_day(m, n)}")



def previous_day(m, n):
    return (datetime(2000, m, n) - timedelta(days=1)).strftime("%d.%m.")


def next_day(m, n):
    return (datetime(2000, m, n) + timedelta(days=1)).strftime("%d.%m.")


m = int(input("Введите номер месяца: "))
n = int(input("Введите число: "))


print(f"Предыдущий день: {previous_day(m, n)}")
print(f"Следующий день: {next_day(m, n)}")
