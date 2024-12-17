def get_month_number(n):
    if 0 <= n <= 11:
        x = n + 1  # Номер месяца от 1 до 12
    else:
        raise ValueError("Количество месяцев должно быть от 0 до 11.")
    return x


n = 3
x = get_month_number(n)
print(f"Месяц: {x}")
