a = True
b = False
c = False
print(f" а) {a and b and not c}")
print(f" б) {not a and not b}")
print(f" в) {not (a and b) or c}")
print(f" г) {a or not b and c}")
print(f" д) {a or (not b and c)}")
print(f" е) {a or (not (b and c))}")
