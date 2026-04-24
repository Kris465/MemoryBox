def get_valid_input():

    while True:
        try:
            n = int(input("Введите число n от 0 до 999: "))
            if 0 <= n <= 999:
                return n
            else:
                print("Введённое число должно быть \
                    в диапазоне от 0 до 999. Попробуйте ещё раз.")
        except ValueError:
            print("Вы ввели некорректное значение. Попробуйте ещё раз.")


def transform_number(n):

    x = ((n - (n % 10)) // 10) + ((n % 10) * 100)
    return x


if __name__ == "__main__":
    n = get_valid_input()
    transformed_value = transform_number(n)
    print(transformed_value)
