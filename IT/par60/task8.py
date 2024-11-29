n = int(input("Введите натуральное число: "))


def factorial(n):
    number = 1
    for i in range(1, n+1):
        number = number * i
    return number


print(factorial(n))
