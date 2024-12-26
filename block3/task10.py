# Исходные значения
A = False
B = False
C = True

# Вычисление значений логических выражений
a = (not A or not B) and not C
b = (not A or not B) and (A or B)
c = A and B or A and C or not C

# Вывод результатов
print("а:", a)
print("б:", b)
print("в:", c)
