X1 = True
Y1 = True
Z1 = True
X2 = False
Y2 = True
Z2 = True
X3 = False
Y3 = False
Z3 = True
X4 = False
Y4 = False
Z4 = False
X5 = False
Y5 = True
Z5 = False
X6 = True
Y6 = False
Z6 = False

# а
print(f'a) {(not X1 or not Y1) or Z1}')
print(f'{(not X2 or not Y2) or Z2}')
print(f'{(not X3 or not Y3) or Z3}')
print(f'{(not X4 or not Y4) or Z4}')
print(f'{(not X5 or not Y5) or Z5}')
print(f'{(not X6 or not Y6) or Z6}')

# б
print(f"б) {Y1 or not X1 or not Z1}")
print(f"{Y2 or not X2 or not Z2}")
print(f"{Y3 or not X3 or not Z3}")
print(f"{Y4 or not X4 or not Z4}")
print(f"{Y5 or not X5 or not Z5}")
print(f"{Y6 or not X6 or not Z6}")

# в
print(f"в) {not Y1 or not X1 or Z1}")
print(f"{not Y2 or not X2 or Z2}")
print(f"{not Y3 or not X3 or Z3}")
print(f"{not Y4 or not X4 or Z4}")
print(f"{not Y5 or not X5 or Z5}")
print(f"{not Y6 or not X6 or Z6}")
