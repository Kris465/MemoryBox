import math

# Ввод значений переменных
a = float(input("Введите a: "))
b = float(input("Введите b: "))

# Расчет функции 1
if b != 0:
    y = 2 * a / b
else:
    y = None
    print("Значение b не должно быть равно 0 для деления.")

# Расчет функции 2
z = 2 * math.sin(5.5 * a + b)

# Вывод результатов
if y is not None:
    print(f"Значение y = {y}")
print(f"Значение z = {z}")
