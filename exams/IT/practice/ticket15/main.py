text = input("Введите сообщение: ")
num1 = int(input("Введите свой номер компьютера: "))
num2 = int(input("Ввкедите номер компьютера, куда хотите отправить: "))


def one():
    print(text)


def two():
    print(text)


def three():
    print(text)


def four():
    print(text)


def five():
    print(text)


def centre():
    if num1 == 1 and num1 != num2:
        print("Начало с первого компьютера")
    elif num1 == 2 and num1 != num2:
        print("Начало со второго компьютера")
    elif num1 == 3 and num1 != num2:
        print("Начало с третьего компьютера")
    elif num1 == 4 and num1 != num2:
        print("Начало с четвёртого компьютера")
    elif num1 == 5 and num1 != num2:
        print("Начало с пятого компьютера")
    elif num1 < 1 and num1 > 5:
        print("Ошибка")
        return
    elif num1 == num2:
        print("Вы на своё компьютер отправили сообщение")
        return
    print("Дошло до центрального компьютера")
    if num2 == 1:
        print("Дошла информация до первого компьютера")
        one()
    elif num2 == 2:
        print("Дошла информация до второго компьютера")
        two()
    elif num2 == 3:
        print("Дошла информация до третьего компьютера")
        three()
    elif num2 == 4:
        print("Дошла информация до четвёртого компьютера")
        four()
    elif num2 == 5:
        print("Дошла информация до пятого компьютера")
        five()


centre()
