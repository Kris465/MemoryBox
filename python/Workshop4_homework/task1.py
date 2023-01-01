# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# def round_func():
#     number = float(input("Input your number, please: "))
#     fractional_part = float(input("Input the sample of your number: "))
#     current = 0

#     while fractional_part != int(fractional_part):
#         fractional_part *= 10
#         current += 1

#     number = round(number, current)
#     print(f"Your number in asked sample: {number}")

# round_func()

# Странное условие. Исправленный вариант, соответствующий заданию:

def number_PI():
    d = int(input("Input the numbers after comma: "))

    PI = 0
    for i in range(1, d * 2 ** 22):
        PI = PI + 4 * ((-1) ** (i + 1)) / (2 * i - 1)
    print(f"PI is: {round(PI, d)}")

number_PI()