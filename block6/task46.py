def analyze_number(num):

    num_str = str(num)

    digits = [int(d) for d in num_str]

    sum_of_digits = sum(digits)
    print("Сумма цифр больше 10: ", sum_of_digits > 10)

    product_of_digits = 1
    for d in digits:
        product_of_digits *= d
    print("Произведение цифр меньше 50: ", product_of_digits < 50)

    num_of_digits = len(digits)
    print("Количество цифр четное: ", num_of_digits % 2 == 0)

    print("Число четырехзначное: ", 1000 <= num < 10000)

    first_digit = digits[0]
    print("Первая цифра не превышает 6: ", first_digit <= 6)

    print("Начинается и заканчивается одной и той же цифрой: ", digits[0] ==
          digits[-1])

    last_digit = digits[-1]
    if first_digit > last_digit:
        print("Первая цифра больше последней")
    elif first_digit < last_digit:
        print("Последняя цифра больше первой")
    else:
        print("Первая и последняя цифры равны")


num = int(input("Введите натуральое число: "))
analyze_number(num)
