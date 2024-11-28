from math import sin, radians, sqrt, cos

a = int(input("напиши число a: "))
b = int(input("напиши число b: "))
c = int(input("напиши число c: "))
x = int(input("напиши число x: "))

print(f'a / b / c = {a/b/c}')
print(f'a * b / c = {a*b/c}')
print(f'a + (b / c) = {a / (b * c)}')
print(f'a + (b * c) = {a + (b / c)}')
print(f'(a / b) / c = {(a + b) / c}')
print(f'a + b / b + c = {a + b/b + c}')
print(f'a + b/b + c = {(a + b) / (b + c)}')
print(f'a / sin(b) = {a / sin(b)}')
print(f'1 / 2 * a * b * sin(x) = {1 / 2 * a * b * sin(x)}')
print(f'2 * b * c * cos a / sin(x) = {2 * b * c * cos(a / x) / (b + c)}')
print(f'4 * 8.31 * sin(a / 2) * sin(b / 2) * sin(c / 2) = {4 * 8.31 * sin(a / 2) * sin(b / 2) * sin(c / 2)}')
print(f'a * x * b / c + d = {a * x * b / (c / b)}')
print(f'2 * sin((a + b) / 2) * cos((a - b) / 2) = {2 * sin((a + b) / 2) * cos((a - b) / 2)}')

