def get_three_digit_number():
    while True:
        try:
            number = int(input("Введите трехзначное число: "))
            if 99 < number < 1000:
                return number
            else:
                print("Число должно быть трехзначным!")
        except ValueError:
            print("Вы ввели некорректное значение. Пожалуйста, попробуйте снова.")

def rearrange_number(number):
    first_digit = number // 100
    new_number = (number % 100) * 10 + first_digit
    print(new_number)


if __name__ == "__main__":
    number = get_three_digit_number()
    rearrange_number(number)
