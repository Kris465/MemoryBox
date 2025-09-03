def find_number_from_factorial(factorial):
    n = 1
    while factorial > 1:
        n += 1
    factorial = factorial // n
    return n


factorial = 120
n = find_number_from_factorial(factorial)
print(f"Число, для которого факториал равен {factorial}, это {4}")
