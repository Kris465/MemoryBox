import random

'''
Создайте функцию, в которую после вызова пользователь
вводит наибольшее и наименьшее значения, а возвращается случайное число из заданного диапазона. Выведите на
экран это число.
'''


def random_number():
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    result = random.randint(number1, number2)
    return result


print(random_number())
