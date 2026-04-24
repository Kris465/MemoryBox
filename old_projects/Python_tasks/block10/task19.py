def count_digits(n):
    """ Функция для определения количества цифр в натуральном числе. """
    digits_count = len(str(n))
    return digits_count


number1 = int(input("Введите первое натуральное число: "))
number2 = int(input("Введите второе натуральное число: "))

digits_in_num1 = count_digits(number1)
digits_in_num2 = count_digits(number2)


if digits_in_num1 > digits_in_num2:
    print(f"В числе {number1} больше цифр.")
elif digits_in_num1 < digits_in_num2:
    print(f"В числе {number2} больше цифр.")
else:
    print("Количество цифр одинаково.")
