x = False
y = True
z = False
print(f"a) {x and not (z or y) or not z}")
print(f"a) {not x or x and (y and z)}")
print(f"a) {(x or y and not z) and z}")
