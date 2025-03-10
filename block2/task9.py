# TODO Нормально обработать ошибку. Таким образом, чтобы программа не падала.

def get_month_number(n):
    if 0 <= n <= 11:
        x = n + 1
    else:
        raise ValueError("Количество месяцев должно быть от 0 до 11.")
    return x


n = int(input("Введите номер месяца: "))
x = get_month_number(n)
print(f"Месяц: {x}")
