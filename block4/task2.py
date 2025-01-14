from math import sin

x = float(input("x="))  # Теперь принимаем вещественное число

if x > 0:
    y = 1 + 2 * sin(x)**2  # Используем синус квадрата x
else:
    y = sin(x**2)          # Синус от квадрата x

print(y)
