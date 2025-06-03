def calculate_age(birth_year, birth_month, current_year, current_month):
    if not (1 <= birth_month <= 12 and 1 <= current_month <= 12):
        raise ValueError("Месяц должен быть от 1 до 12")

    age_years = current_year - birth_year
    age_months = current_month - birth_month

    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months


birth_year = int(input("Введите год рождения: "))
birth_month = int(input("Введите номер месяца рождения (1-12): "))
current_year = int(input("Введите текущий год: "))
current_month = int(input("Введите номер текущего месяца (1-12): "))


age_years, age_months = calculate_age(birth_year, birth_month,
                                      current_year, current_month)


print(f"Ваш возраст: {age_years} лет, {age_months} месяцев")
