# Массив с годами рождения 30 человек
birth_years = [/* вставьте сюда ваши данные: 30 чисел */]

current_year = 2024

# Находим минимальный и максимальный год рождения
min_year = min(birth_years)
max_year = max(birth_years)

# Вычисляем возраст старейшего и младшего
age_oldest = current_year - min_year
age_youngest = current_year - max_year

# Разница в возрасте
age_difference = age_oldest - age_youngest

print("Возраст самого старого человека \
    превышает возраст самого молодого на:", age_difference)