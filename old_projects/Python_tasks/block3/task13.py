A = False
B = False
C = True
D = True
E = True
F = False
G = False
H = True

# a
print(f"a) {not (A and B)}")
print(f"{not (C and D)}")
print(f"{not (E and F)}")
print(f"{not (G and H)}")

# б
print(f"б) {not A or B}")
print(f"{not C or D}")
print(f"{not E or F}")
print(f"{not G or H}")

# в
print(f"в) {A or not B}")
print(f"{C or not D}")
print(f"{E or not F}")
print(f"{G or not H}")
