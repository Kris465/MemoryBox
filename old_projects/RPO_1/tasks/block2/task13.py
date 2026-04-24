num = int(input("Введите трехзначное число: "))
if 100 <= num <= 999:
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    reversed_num = c * 100 + b * 10 + a
    print("Число, прочитанное справа налево:", reversed_num)
else:
    print("Ошибка: введите именно трехзначное число.")