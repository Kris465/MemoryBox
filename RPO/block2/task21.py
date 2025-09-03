def get_number_greater_than_nine():

    while True:
        try:
            number = int(input("Напишите число больше 9: "))
            if number > 9:
                return number
            else:
                print("Число должно быть больше 9!")
        except ValueError:
            print("Вы ввели некорректное значение. Попробуйте ещё раз.")


def extract_tens_and_units(number):

    tens = (number // 10) % 10
    units = number % 10
    return tens, units


def display_results(tens, units):

    print(f"Десятки в этом числе: {tens}")
    print(f"Единицы в этом числе: {units}")


if __name__ == "__main__":

    number = get_number_greater_than_nine()

    tens, units = extract_tens_and_units(number)

    display_results(tens, units)
