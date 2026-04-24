number = int(input("Введите двухзначное число: "))
number_str = str(number)

if '4' in number_str or '7' in number_str:
    print("а) числа 4 или 7 входят в число")
else:
    print("а) числа 4 и 7 не входят в число")

if '3' in number_str or '6' in number_str or '9' in number_str:
    print("б) числа 3,6 или 9 входят в число")
else:
    print("б) числа 3,6 и 9 не входят в число")
