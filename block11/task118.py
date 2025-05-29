# Массив с годами рождения 30 человек
birth_years = [/* вставьте сюда ваши данные: 30 чисел */]

# Находим минимальный год рождения (самый старший)
min_year = min(birth_years)

# а) номер первого человека с этим годом
first_oldest_index = birth_years.index(min_year) + 1

# б) номер последнего человека с этим годом
last_oldest_index = len(birth_years) - 1 - birth_years[::-1].index(min_year) + 1

print("Порядковый номер самого старшего (первый случай):", first_oldest_index)
print("Порядковый номер самого старшего (последний случай):", last_oldest_index)
