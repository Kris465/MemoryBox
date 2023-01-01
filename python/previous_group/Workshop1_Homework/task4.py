# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!

# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0

# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

def calculator():
    num1 = float(input("Input the first number: "))
    operator = input("Input the operation: ")
    num2 = float(input("Input the second number: "))

    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2) 
    elif operator == 'pov':
        print(num1 ** num2)
    elif num2 != 0:
        if operator == '/':
            print(num1 / num2)
        elif operator == 'mod':
            print(num1 % num2)
        elif operator == 'div':
            print(num1 // num2)
    else: print("Divine for zero.")

calculator()