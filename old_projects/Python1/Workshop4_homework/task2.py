# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

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

    print(f"The multipliers of your number is:", *multipliers)

simple_multipliers()
