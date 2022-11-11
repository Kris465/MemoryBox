# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*

# 2+2 => 4;

# 1+2*3 => 7;
# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

# *Пример:*

# 1+2*3 => 7;

# (1+2)*3 => 9;

def calc():
    action = input("Input you operation. Please separate numbers from the sign of operation with space: ")
    data = action.split()
    sign = data[1]
    data = list(filter(lambda x: str(x).isdigit(), data))

    if sign == "*":
        answer = int(data[0]) * int(data[1])
    elif sign == "/":
        answer = [int(data[0]) / int(data[1]) if int(data[1]) != 0 and sign == "/" else print("Division for zero is forbidden. It's sad, sorry.")]
    elif sign == "+" or "-":
        answer = [int(data[0]) - int(data[1]) if sign == "-" else int(data[0]) + int(data[1])]
    else: print("I don't know this sign, try again.")

    if sign == "*":
        print(f"Your answer is: {answer}")
    else: print("Your answer is:", *answer)

calc()