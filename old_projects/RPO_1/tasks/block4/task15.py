birth_year = int(input("Введите год рождения: "))
birth_month = int(input("Введите номер месяца рождения (1-12): "))

current_year = int(input("Введите текущий год: "))
current_month = int(input("Введите текущий месяц (1-12): "))

if current_month > birth_month:
    age = current_year - birth_year
elif current_month == birth_month:

    age = current_year - birth_year
else:
    age = current_year - birth_year - 1

print(f"Возраст человека: {age} лет")
