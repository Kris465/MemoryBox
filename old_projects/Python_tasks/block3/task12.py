# a
x = 1
y = -1
print(f"{x * x - y - y <= 0}")

# б
x = 2
y = 2
print(f"{(x >= 2) or (y * y != 4)}")

# в
x = 2
y = 2
print(f"{(x >= 0) and (y * y > 4)}")

# г
x = 1
y = 2
print(f"{(x * y != 4) and (y > x)}")

# д
x = 2
y = 1
print(f"{(x * y != 0) or (y < x)}")

# е
x = 1
y = 2
print(f"{(not (x * y < 1)) and (y > x)}")

# ж
x = 2
y = 1
print(f"{(not (x * y < 0)) or (y > x)}")
