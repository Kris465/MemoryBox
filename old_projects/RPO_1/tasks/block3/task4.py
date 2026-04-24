# Задаем логические величины
X = True  # Истина
Y = True   # Истина
Z = False  # Ложь

result_a = not X and Y  # а) X или Z
result_b = X or not Y # б) X и Y
result_c = X or Y and Z  # в) X и Z

print("Значение логического выражения А", result_a)
print("Значение логического выражения Б", result_b)
print("Значение логического выражения В", result_c)
