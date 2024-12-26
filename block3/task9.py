# Исходные значения
X = True
Y = False
Z = False

# Вычисление значений логических выражений
a = not X or not Y or not Z
b = (not X or not Y) and (X or Y)
c = X and Y or X and Z or not Z

# Вывод результатов
print("а:", a)
print("б:", b)
print("в:", c)
