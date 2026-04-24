birth_day = int(input("Введите день (1 - 31) рождения: "))
birth_month = int(input("Введите месяц (1 - 12) рождения: "))
birth_year = int(input("Введите год рождения: "))

current_day = int(input("Введите настоящий день: "))
current_month = int(input("Введите настоящий месяц: "))
current_year = int(input("Введите настоящий год: "))


age = current_year - birth_year


if (current_month, current_day) < (birth_month, birth_day):
    age -= 1


print(f'Возраст человека - {age}')
