
A = True
B = False
C = False


a = A or not (A and B) or C
b = not A or A and (B or C)
c = (A or B and not C) and C


print("а)", a)
print("б)", b)
print("в)", c)
