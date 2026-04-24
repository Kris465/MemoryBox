from math import sqrt

a = int(input("Введите число a:"))
b = int(input("Введите число b:"))

srednee_matem = abs(a) + abs(b) / 2  
srednee_geometr = sqrt(abs(a) + abs(b))


print(srednee_matem)
print(srednee_geometr)