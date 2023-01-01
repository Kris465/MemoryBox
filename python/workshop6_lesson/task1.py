# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*

# 2+2 => 4;

# 1+2*3 => 7;
# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

# *Пример:*

# 1+2*3 => 7;

# (1+2)*3 => 9;

def calculate(a, b, operation):
    result = None

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "/":
        result = a / b
    elif operation == "*":
        result = a * b
    else:
        print("Unknown operation.")

    return result

def f3_1():
    str_operation = " /"
    a = float(input("Input the first number: "))
    b = float(input("Input the second number: "))
    operation = input(f"Input operation {str_operation}: ")
    res = calculate(a, b, operation)
    print(res)

f3_1()