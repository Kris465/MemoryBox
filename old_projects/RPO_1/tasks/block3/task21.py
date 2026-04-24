A = input("Введите true или false: ")
B = input("Введите true или false: ")
C = input("Введите true или false: ")
rez1 = not (A or not B and C)
rez2 = A and not (B and not C)
rez3 = not (not A or B and not C)

print("a)", rez1)
print("б)", rez2)
print("в)", rez3)
# Вычислить значение логического выражения при всех возможных значениях
# а) не (А или не В и С);
# б) А и не (В и или не С);
# в) не (не А или В и С).
