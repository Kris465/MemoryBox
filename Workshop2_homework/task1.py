# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def sum_of_digits():
    number = float(input("Input your number, please: "))
    digits = 0

    if number // 10 != 0 and (number * 10) % 10 != 0:
        while (number * 10) % 10 != 0:
            number *= 10
        while number != 0:
            digits += number % 10 
            number = number // 10
            print(int(digits))
    elif number // 10 != 0:
        while number != 0:
            digits += number % 10 
            number = number // 10
            print(int(digits))
    else: 
        while number % 10 == 0:
            number = number * 10
            digits += number % 10 
            print(int(digits))

sum_of_digits()