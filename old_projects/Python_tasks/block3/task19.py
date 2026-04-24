A = True
B = True
C = False
D = False
E = True
F = False
G = False
H = True

print(f"А){not (not A and not B) and A}")
print(f"{not (not C and not D) and C}")
print(f"{not (not E and not F) and E}")
print(f"{not (not G and not H) and G}")

print(f"Б){not (not A or not B) and A}")
print(f"{not (not C or not D) and C}")
print(f"{not (not E or not F) and E}")
print(f"{not (not G or not H) and G}")

print(f"В){not (not A or not B) and B}")
print(f"{not (not C or not D) and D}")
print(f"{not (not E or not F) and F}")
print(f"{not (not G or not H) and H}")
