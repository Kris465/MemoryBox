def get_three_digit_number():

    while True:
        try:
            number = int(input("Введите трёхзначное число: "))
            if 99 < number < 1000:
                return number
            else:
                print("Введённое число должно быть трёхзначным!")
        except ValueError:
            print("Вы ввели некорректное значение. Попробуйте ещё раз.")


def rearrange_digits(number):

    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10
    return f"{hundreds}{units}{tens}"


if __name__ == "__main__":

    three_digit_number = get_three_digit_number()

    rearranged_number = rearrange_digits(three_digit_number)
    print(rearranged_number)
