number = input("введите число")


if len(number) != 4:
    print("неверный ввод.должно быть 4.")
else:
    for digit in set(number):
        if number.count(digit) == 3:
            print(f'число {number} содержит ровно три олинаковых цифры.')
            break
    else:
        print(f"число {number} не содержит ровно три одинаковых числа.")
