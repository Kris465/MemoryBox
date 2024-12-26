# Исходные значения
A = True
B = False
C = False

# Вычисление значений логических выражений
a = A or (B and not C)
b = not A and not B
c = not (A and C) or B
d = A and (not B or C)
e = A or not (B and C)

# Вывод результатов
print("а:", a)
print("б:", b)
print("в:", c)
print("г:", d)
print("е:", e)
