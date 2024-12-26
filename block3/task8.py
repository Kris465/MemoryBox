# Исходные значения
X = False
Y = True
Z = False

# Вычисление значений логических выражений
a = X and not (Z or Y) or not Z
b = not X or X and (Y or Z)
c = (X or Y and not Z) and Z

# Вывод результатов
print("а:", a)
print("б:", b)
print("в:", c)
