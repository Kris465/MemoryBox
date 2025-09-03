day = int(input("Введите номер дня: "))

if day % 7 == 0:
    print("Воскресенье")
elif (day + 1) % 7 == 0:
    print("Суббота")
elif (day + 2) % 7 == 0:
    print("Пятница")
elif (day + 3) % 7 == 0:
    print("Четверг")
elif (day + 4) % 7 == 0:
    print("Среда")
elif (day + 5) % 7 == 0:
    print("Вторник")
elif (day + 6) % 7 == 0:
    print("Понедельник")
