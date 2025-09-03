def digit_sum(n):
    """
    Функция вычисляет сумму цифр натурального числа n.
    """
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


number1 = int(input('Введите первое натуральное число: '))
number2 = int(input('Введите второе натуральное число: '))


sum_digits1 = digit_sum(number1)
sum_digits2 = digit_sum(number2)


if sum_digits1 > sum_digits2:
    print(f'В первом числе ({number1}) сумма цифр больше.')
elif sum_digits1 < sum_digits2:
    print(f'Во втором числе ({number2}) сумма цифр больше.')
else:
    print('Суммы цифр в обоих числах одинаковы.')
