def sum_of_digits_squared_equals_m(m, n):
    results = []
    for number in range(1, n):
        digit_sum = sum(int(digit) for digit in str(number))
        if digit_sum ** 2 == m:
            results.append(number)
    return results


m = int(input("Введите значение m: "))
n = int(input("Введите значение n: "))
results = sum_of_digits_squared_equals_m(m, n)
print("Натуральные числа, меньшие n, квадрат суммы цифр которых равен m:")
print(results)
