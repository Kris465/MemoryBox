number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))

if number1 >= number2 and number1 >= number3:
    print(f"Сумма меньших чисел равна: {number2 * number3}")
elif number2 >= number1 and number2 >= number3:
    print(f"Сумма меньших чисел равна: {number1 * number3}")
else:
    print(f"Сумма меньших чисел равна: {number1 * number2}")
