A = input("Введите A: ")
B = input("Введите B: ")
a = not A or not B
b = A and (A or not B)
c = (not A or B) and B

print("а)", a)
print("б)", b)
print("в)", c)
