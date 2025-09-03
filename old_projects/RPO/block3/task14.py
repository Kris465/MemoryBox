X = True
Y = False
A = True
B = True
C = False
D = False
E = False
F = True

print(f"a){not {X or Y}}")
print(f"{not {A or B}}")
print(f"{not {C or D}}")
print(f"{not {E or F}}")

print(f"б){not X and Y}")
print(f"{not A and B}")
print(f"{not C and D}")
print(f"{not E and F}")

print(f"в){X and not Y}")
print(f"{A and not B}")
print(f"{C and not D}")
print(f"{E and not F}")
