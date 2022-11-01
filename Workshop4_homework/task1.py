# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def round_func():
    number = float(input("Input your number, please: "))
    fractional_part = float(input("Input the sample of your number: "))
    current = 0

    while fractional_part != int(fractional_part):
        fractional_part *= 10
        current += 1

    number = round(number, current)
    print(number)


round_func()