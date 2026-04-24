k = int(input("Введите номер карты (2 - 14)"))


def nomer(k):
    match k:
        case 2:
            return "Двойка"
        case 3:
            return "Тройка"
        case 4:
            return "Четверка"
        case 5:
            return "Пятерка"
        case 6:
            return "Шестёрка"
        case 7:
            return "Семёрка"
        case 8:
            return "Восьмёрка"
        case 9:
            return "Девятка"
        case 10:
            return "Десятка"
        case 11:
            return "Валет"
        case 12:
            return "Дама"
        case 13:
            return "Король"
        case 14:
            return "Туз"
        case _:
            return "Недопустимый номер карты"


print("Достоинство карты:", nomer(k))
