num = int(input("Введите трехзначное число: "))
if 100 <= num <= 999:
    first_digit = num // 100
    last_two_digits = num % 100
    new_num = last_two_digits * 10 + first_digit
    print("Полученное число:", new_num)
else:
    print("Ошибка: введите именно трехзначное число.")
