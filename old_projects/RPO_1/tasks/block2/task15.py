num = int(input("Введите трехзначное число: "))
if 100 <= num <= 999:
    last_digit = num % 10
    first_two_digits = num // 10
    new_num = last_digit * 100 + first_two_digits
    print("Полученное число:", new_num)
else:
    print("Ошибка: введите именно трехзначное число.")