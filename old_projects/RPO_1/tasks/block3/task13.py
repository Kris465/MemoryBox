# Вычислить значение логического выражения при всех возможных значениях
# логических величин А и В:
# а) не (А и В);
# б) не А или В;
# в) А или не В.
A = input("Введите true или false: ")
B = input("Введите true или false: ")
C = input("Введите true или false: ")
rez1 = not (A and B)
rez2 = not A or B
rez3 = A or not B

print("a)", rez1)
print("б)", rez2)
print("в)", rez3)
