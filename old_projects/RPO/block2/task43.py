def check_divisibility(a, b):

    result = (a % b == 0) or (b % a == 0)
    return 1 if result else 0


def get_integer_input(prompt):

    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")


if __name__ == "__main__":

    a = get_integer_input("Введите число a: ")
    b = get_integer_input("Введите число b: ")

    output = check_divisibility(a, b)
    print(output)
