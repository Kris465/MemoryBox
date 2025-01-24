from datetime import date, timedelta


start_date = date(1990, 1, 1)


n = int(input("введите количество месяцев: "))


end_date = start_date + timedelta(days=n * 30 + 2)


month_names = ["Я", "ф", "М", "А", "Май", "Июнь", "Июль", "Авг", "C", "о", "Н",
               "Д"]


print(f"Название месяца: {month_names[end_date.month - 1]}")
