two = int(input("Введите двухзначное число: "))
a = int(input("Введите цифру a: "))
two_str = str(two)
a_str = str(a)
if "3" in two_str:
    print("Цифра 3 есть в числе")
else:
    print("Цифры 3 нету в числе")
if a_str in two_str:
    print("Цифра a есть в числе")
else:
    print("Цифры a нету в числе")
