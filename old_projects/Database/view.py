def view():
    print("Я беру и вывожу ваше число!")
    choose = int(input("1 - ввести число\n2 - выход\n"))
    match choose:
        case 1:
            input_number = int(input("Введите ваше число: "))
        case 2:
            input_number = 2
        case _:
            input_number = "Неправильный выпор, попробуйте снова!"
    return input_number
