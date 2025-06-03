def reverse_and_print(number):
    reversed_str = str(number)[::-1]
    reversed_num = int(reversed_str)
    print(reversed_num)


def get_user_input():
    while True:
        user_input = input('Введите число: ')

        try:
            number = int(user_input)
            reverse_and_print(number)
            break
        except ValueError:
            print("Ошибка! Введенное значение должно быть числом. \
                Попробуйте еще раз.")


if __name__ == "__main__":
    get_user_input()
