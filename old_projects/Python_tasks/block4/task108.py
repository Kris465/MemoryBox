masit = ["Пики", "Трефы", "Бубны", "Черви"]

n = int(input("Введите номер масти (1-4): "))

match n:
    case 1:
        print("ПИКИ")
    case 2:
        print("ТРЕФЫ")
    case 3:
        print("БУБНЫ")
    case 4:
        print("ЧЕРВИ")
    case _:
        print("Ошибка не найдено")
