grades = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
count_fives = len(grades) - grades.index(4) if 4 in grades else len(grades)
print(count_fives)
