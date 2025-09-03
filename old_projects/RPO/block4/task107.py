def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def get_days_in_month(month, leap_year=False):
    if month == 2:
        return 29 if leap_year else 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31


# Ввод месяца
try:
    month = int(input("Введите номер месяца (от 1 до 12): "))
    if not 1 <= month <= 12:
        raise ValueError("Месяц должен быть от 1 до 12.")
except ValueError as e:
    print(f"Ошибка ввода месяца: {e}")
    exit()

# Ввод года
year_input = input("Введите год (или нажмите Enter, если не знаете точно): ")
leap_year = False

if year_input:
    try:
        year = int(year_input)
        leap_year = is_leap_year(year)
    except ValueError:
        print("Вы ввели некорректный год. Будет использован невисокосный год.")


# Получаем количество дней
days = get_days_in_month(month, leap_year)
print(f"В этом месяце {days} дней.")
