def is_precipitation_higher(current_year, last_year):
    return sum(current_year) > sum(last_year)


current_year = [5, 10, 15, 20]
last_year = [4, 9, 14, 19]
result = is_precipitation_higher(current_year, last_year)
print(f"Осадки текущего года превысили прошлогодние: {result}")
