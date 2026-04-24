import math

x = float(input("Введите значение x: "))

if x == 2:
    y = math.sin(2)
else:
    y = 1 + 2 * math.sin(x)

print(f"При x = {x}, y = {y}")
