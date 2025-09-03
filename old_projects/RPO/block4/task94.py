points = int(input("Введите количество очков (0,1,3): "))


if points == 0 or 1 or 3:
    if points == 0:
        print("Проигрыш")
    if points == 1:
        print("Ничья")
    if points == 3:
        print("Победа")

if points != 0 or 1 or 3:
    print("Ошибка")
