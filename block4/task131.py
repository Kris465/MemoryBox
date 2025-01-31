def calculate_age(birth_year, birth_month, current_year, current_month):
    age_years = current_year - birth_year
    age_months = current_month - birth_month
    if age_months < 0:
       age_years -= 1
    return age_years, age_months


birth_year = int(input("Введите год рождения: "))
birth_month = int(input("Введите номер месяца рождения: "))
current_year = int(input("Введите текущий год: "))
current_month = int(input("Введите текущий месяц:"))

age_years, age_months = calculate_age(birth_year, birth_month,
                                      current_year, current_month)
print(f"Ваш возраст: {age_years} лет, {abs(age_months)} месяцев")
