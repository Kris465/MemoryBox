import math

a = 1.0

y_a = 2 * math.sin(abs(3 * a)) + 3.56 * a
print(f"Значение функции y = 2*sin(|3a|) + 3.56*a при a = {a} равно {y_a}")


x = 1.0
if x != 0:
    y_b = 3.2 + math.sin(abs(5 / x))
    print(f"Значение функции y = 3.2 + sin(|5/x|) при x = {x} равно {y_b}")
else:
    print("Ошибка: x не должен быть равен 0, деление на ноль невозможно.")
