x = 1
y = -1
a = x ** 2 - y ** 2
print(a)

x = 2
y = -2
b = x >= 2 or y ** 2 != 4
print(b)

x = 2
y = 2
v = x >= 0 and y ** 2 > 4
print(v)

x = 1
y = 2
g = x * y != 4 and y > x
print(g)

x = 2
y = 1
d = x * y != 0 or y < x
print(d)

x = 1
y = 2
e = not x * y < 1 and y > x
print(e)

x = 2
y = 1
zh = not x * y < 0 or y > x
print(zh)
