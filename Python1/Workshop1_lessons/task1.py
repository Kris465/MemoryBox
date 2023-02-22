# 1. Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.

def sqrt_num():
    number1 = int(input("Input the first number: "))
    number2 = int(input("Input the second number: "))

    if number2 == number1 ** number1 or number1 == number2 ** number2:
        print("Yes")
    else: 
        print("No")

sqrt_num()