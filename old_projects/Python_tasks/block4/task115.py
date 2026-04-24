y = int(input("Введите год: "))
cy = (y - 4) % 60
q = cy % 12
t = cy % 10
match t:
    case 0:
        print("Зелёный", end=' ')
    case 1:
        print("Зелёный", end=' ')
    case 2:
        print("Красный", end=' ')
    case 3:
        print("Красный", end=' ')
    case 4:
        print("Жёлтый", end=' ')
    case 5:
        print("Жёлтый", end=' ')
    case 6:
        print("Белый", end=' ')
    case 7:
        print("Белый", end=' ')
    case 8:
        print("Чёрный", end=' ')
    case 9:
        print("Чёрный", end=' ')
match q:
    case 0:
        print("Крыса", end=' ')
    case 1:
        print("Корова", end=' ')
    case 2:
        print("Тигр", end=' ')
    case 3:
        print("Заяц", end=' ')
    case 4:
        print("Дракон", end=' ')
    case 5:
        print("Змея", end=' ')
    case 6:
        print("Лошадь", end=' ')
    case 7:
        print("Овца", end=' ')
    case 8:
        print("Обезьяна", end=' ')
    case 9:
        print("Петух", end=' ')
    case 10:
        print("Собака", end=' ')
    case 11:
        print("Свинья", end=' ')
