a = True
b = True
c = False
f = False
g = False
d = True
v = True
m = False

# a
print(f'a) {not a or not b}')
print(f'{not c or not f}')
print(f'{not g or not d}')
print(f'{not v or not m}')

# Б
print(f'Б) {a and (a or not b)}')
print(f'{c and (c or not f)}')
print(f'{g and (g or not d)}')
print(f'{v and (v or not m)}')

# В
print(f'В) {(not a or b) and b}')
print(f'{(not c or f) and f}')
print(f'{(not g or d) and d}')
print(f'{(not v or m) and m}')
