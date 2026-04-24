def get_number_greater_than_99():

    while True:
        try:
            number = int(input("Введите число больше 99: "))
            if number > 99:
                return number
            else:
                print("Число должно быть больше 99!")
        except ValueError:
            print("Вы ввели некорректное значение. Попробуйте ещё раз.")


def extract_hundreds_and_tens(number):

    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    return tens, hundreds


def display_results(tens, hundreds):

    print("а) Десятков = ", tens)
    print("б) Сотен = ", hundreds)


if __name__ == "__main__":

    number = get_number_greater_than_99()

    tens, hundreds = extract_hundreds_and_tens(number)

    display_results(tens, hundreds)
