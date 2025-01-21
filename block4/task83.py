num1 = float(input("Введите первое вещественное число: "))
num2 = float(input("Введите второе вещественное число: "))
num3 = float(input("Введите третье вещественное число: "))
num4 = float(input("Введите четвертое вещественное число: "))
numbers = num1, num2, num3, num4


def sum_greater_than_five(numbers):
    return sum(filter(lambda x: x > 5, numbers))


result = sum_greater_than_five(numbers)
print("Сумма чисел больше пяти:", result)
