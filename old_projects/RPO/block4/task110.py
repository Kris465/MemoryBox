m = int(input("Введите число от 1 до 4: "))
k = int(input("Введите число от 6 до 14: "))
if m == 1:
    mast = "пик"
elif m == 2:
    mast = "треф"
elif m == 3:
    mast = "бубен"
elif m == 4:
    mast = "черв"
else:
    print("Ошибка число должно быть от 1 до 4")

if k == 6:
    znach = "Шестерка"
elif k == 7:
    znach = "Семерка"
elif k == 8:
    znach = "Восмерка"
elif k == 9:
    znach = "Девятка"
elif k == 10:
    znach = "Десятка"
elif k == 11:
    znach = "Валет"
elif k == 12:
    znach = "Дама"
elif k == 13:
    znach = "Король"
elif k == 14:
    znach = "Туз"
else:
    print("Ошибка число должно быть от 6 до 14")

print(F"Это карта: {znach} {mast}")
