X = False
Y = False
Z = True

# a)
print(f"{X or Y and not Z}")

# б)
print(f"{not X and not Y}")

# в)
print(f"{not (X and Z) or Y}")

# г)
print(f"{X and not Y or Z}")

# д)
print(f"{X and (not Y or Z)}")

# е)
print(f"{X or (not (Y or Z))}")
