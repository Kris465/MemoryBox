# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibbonachi_func():
    number = int(input("Input your number: "))
    fibo = []
    sum_up = 0
    num1 = 1
    num2 = 1
    
    for i in range(number):
        fibo.append(num1)
        sum_up = num1 + num2
        num1 = num2
        num2 = sum_up
    
    num1 = 0
    num2 = 1
    
    for i in range(number + 1):
        fibo.insert(0, num1)
        sum_up = num1 - num2
        num1 = num2
        num2 = sum_up

    print(f"Asked list is: {fibo}")

fibbonachi_func()