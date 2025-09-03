def get_three_digit_number():

    while True:
        try:
            number = int(input("Введите трёхзначное число: "))
            if 99 < number < 1000:
                return number
            else:
                print("Число должно быть трёхзначным!")
        except ValueError:
            print("Введены некорректные данные. Пожалуйста, \
                введите целое число.")


def process_number(number):

    last_digit = number % 10
    new_number = last_digit * 100 + number // 10
    print(new_number)


if __name__ == "__main__":
    number = get_three_digit_number()
    process_number(number)
