def validate_input(prompt, condition=lambda x: True):

    while True:
        try:
            value = input(prompt)
            if condition(value):
                return value
            else:
                print("Введённое значение не соответствует \
                    условиям. Попробуйте ещё раз.")
        except ValueError:
            print("Введены некорректные данные. Попробуйте ещё раз.")


def add_to_dozen(num1, num2):

    a2 = int(num1[0])
    a1 = int(num1[1])
    b = int(num2)
    s = a1 + b
    if s >= 10:
        a2 += 1
        s -= 10

    return f"{a2}{s}"


if __name__ == "__main__":

    num1 = validate_input("Введите двузначное \
        число: ", lambda x: len(x) == 2 and x.isdigit())

    num2 = validate_input("Введите однозначное \
        число: ", lambda x: len(x) == 1 and x.isdigit())

    result = add_to_dozen(num1, num2)
    print(f"Ответ: {result}")
