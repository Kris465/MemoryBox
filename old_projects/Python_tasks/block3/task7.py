a = True
b = False
c = False
print(f"а) {a or not (a and b) or c}")
print(f"б) {not b or a and (b or c)}")
print(f"в) {(a or b and not c) or c}")
