number = int(input("Введите четырёхзначное число: "))

contains_4or_7 = '4' in str(number) or '7' in str(number)


contains_3_6_9 = '3' in str(number) or '6' in str(number) or '9' in str(number)

if contains_4or_7:
    print("Цифры 4 или 7 входят в число")
else:
    print("Цифры 4 или 7 не входят в число")

if contains_3_6_9:
    print("Цифры 3, 6 или 9 входят в число.")
else:
    print("Цифры 3, 6 или 9 не входят в число.")
