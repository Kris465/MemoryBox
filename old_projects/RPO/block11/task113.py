
birth_years = [list(map(int, input("Введите массив: ").split()))]

current_year = 2024


min_year = min(birth_years)
max_year = max(birth_years)


age_oldest = current_year - min_year
age_youngest = current_year - max_year


age_difference = age_oldest - age_youngest

print("Возраст самого старого человека \
    превышает возраст самого молодого на:", age_difference)
