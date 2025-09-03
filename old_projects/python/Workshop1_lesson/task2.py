# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

def square_numbers():
    number1 = int(input("Input the first number: "))
    number2 = int(input("Input the second number: "))

    if number1 * number1 == number2 or number2 * number2 == number1:
        print("Yes")
    else: print("No")

square_numbers()