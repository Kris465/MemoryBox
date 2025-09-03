A = False
B = False
C = True

a = (not A or not B) and not C
b = (not A or not B) and (A or B)
c = A or B or A and C or not C

print(f'a) {a}')
print(f'b) {b}')
print(f'c) {c}')
