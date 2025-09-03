def get_three_digit_number():
    while True:
        try:
            number = int(input('Введите трехзначное число: '))
            if 99 < number < 1000:
                return number
            else:
                print("Число должно быть трехзначным!")
        except ValueError:
            print("Вы ввели некорректное значение. \
                Пожалуйста, попробуйте снова.")


def split_digits_and_sum(number):
    sto = number // 100
    des = (number // 10) % 10
    ed = number % 10
    sum_digits = sto + des + ed
    print(f'Число единиц = {ed}, число десятков = {des}, \
        а сумма равна = {sum_digits}')


if __name__ == "__main__":
    number = get_three_digit_number()
    split_digits_and_sum(number)
