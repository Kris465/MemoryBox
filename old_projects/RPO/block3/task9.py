X = True
Y = False
Z = False

a = not X or not Y or not Z
b = (not X or not Y) and (X or Y)
c = X and Y or X and Z or not Z

print("а:", a)
print("б:", b)
print("в:", c)
