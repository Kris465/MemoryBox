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
print(f'4 * round * sin(a / 2) * sin(b / 2) * sin(c / 2) = {4 * round * sin(a / 2) * sin(b / 2) * sin(c / 2)}')


