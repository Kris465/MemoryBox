# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def set_of_multi():
    n = int(input("Input your number, please: "))
    ls = []
    result = 1

    for i in range(1, n + 1):
        result *= i
        ls.append(result)
    print(f"Yout list is: {ls}") 

set_of_multi()