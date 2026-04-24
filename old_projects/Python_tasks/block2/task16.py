def get_three_digit_number():

    while True:
        try:
            x = int(input('Введите трёхзначное число: '))
            if 99 < x < 1000:
                return x
            else:
                print("Введённое число должно быть трёхзначным!")
        except ValueError:
            print("Введён некорректный тип данных. Попробуйте ещё раз.")


def rearrange_number(x):

    f = x // 100
    s = x % 100 // 10
    t = x % 10
    return s * 100 + f * 10 + t


if __name__ == "__main__":
    x = get_three_digit_number()
    result = rearrange_number(x)
    print(result)
