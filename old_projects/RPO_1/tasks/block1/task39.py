import math

x = float(input("Введите значение x: "))

f = x**2
g = math.sin(x)

if x > 0:
    y = math.log(x)
else:
    y = None
    print("Логарифм определён только для положительных чисел.")

print(f"f(x) = x^2 = {round(f, 2)}")
print(f"g(x) = sin(x) = {round(g, 2)}")

if y is not None:
    print(f"h(x) = log(x) = {round(y, 2)}")
