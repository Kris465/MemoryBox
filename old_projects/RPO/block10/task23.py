from datetime import date, timedelta


def get_previous_date(g, m, n):
    """
    Функция для получения даты предыдущего дня.
    Параметры:
    g -- год
    m -- месяц
    n -- день
    """
    current_date = date(g, m, n)
    previous_date = current_date - timedelta(days=1)
    return previous_date.year, previous_date.month, previous_date.day


def get_next_date(g, m, n):
    current_date = date(g, m, n)
    next_date = current_date + timedelta(days=1)
    return next_date.year, next_date.month, next_date.day


g = int(input("Введите год: "))
m = int(input("Введите месяц: "))
n = int(input("Введите день: "))

prev_g, prev_m, prev_n = get_previous_date(g, m, n)
next_g, next_m, next_n = get_next_date(g, m, n)

print(f"Предыдущая дата: {prev_g}-{prev_m}-{prev_n}")
print(f"Следующая дата: {next_g}-{next_m}-{next_n}")
