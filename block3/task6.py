# Исходные значения
X = False
Y = False
Z = True

# Вычисление значений логических выражений
a = X or (Y and not Z)
b = not X and not Y
c = not (X and Z) or Y
d = X and (not Y or Z)
e = X or not (Y or Z)

# Вывод результатов
print("а:", a)
print("б:", b)
print("в:", c)
print("г:", d)
print("е:", e)
