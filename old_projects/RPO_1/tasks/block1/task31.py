import math

num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

# Вычисление среднее арифметическое
average_arithmetic = (num1 + num2) / 2


if num1 >= 0 and num2 >= 0:
    average_geometric = math.sqrt(num1 * num2)
else:
    average_geometric = None
print("Среднее геометрическое существует только для неотрицательных чисел.")


print(f"Среднее арифметическое: {average_arithmetic}")
if average_geometric is not None:
    print(f"Среднее геометрическое: {average_geometric}")
