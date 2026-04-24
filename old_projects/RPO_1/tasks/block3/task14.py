# Вычислить значение логического выражение при всех возможных значениях
# логических величин x и y
# a) не (x или y)
# б) не (x и y)
# в) x и не y
x = input("Введите true или false: ")
y = input("Введите true или false: ")
rez1 = not (x or y)
rez2 = not x and y
rez3 = x and not y

print("a)", rez1)
print("б)", rez2)
print("в)", rez3)
