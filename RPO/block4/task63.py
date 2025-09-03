four = int(input("Введите четырёхзначное число: "))
four_0 = four // 1000
four_1 = (four // 100) % 10
four_2 = (four % 100) // 10
four_3 = four % 10
if four_0 == four_1 or four_0 == four_2 or four_0 == four_3 or\
     four_1 == four_2 or four_1 == four_3 or four_2 == four_3:
    print("Нет, какие-то цифры одинаковые")
else:
    print("Да, все цифры разные")
