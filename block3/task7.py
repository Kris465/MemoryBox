A = True
B = False
C = False

# Вычисление значений логических выражений
a = A or not (A and B) or C
b = not A or A and (B or C)
c = (A or B and not C) and C

# Вывод результатов
print("а:", a)
print("б:", b)
print("в:", c)
