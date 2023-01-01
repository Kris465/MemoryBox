# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_multipliers():
    number = int(input("Input yout number, please: "))
    multipliers = []
    a = 2

    while number > 1:
        if number % a == 0:
            multipliers.append(a)
            number /= a
        else:
            a += 1

    print("The multipliers of your number is:", *multipliers)

simple_multipliers()