def get_three_digit_number():

    while True:
        try:
            number = input("Введите трёхзначное число: ")
            if len(number) == 3 and number.isdigit():
                return number
            else:
                print("Введённое значение должно быть трёхзначным числом. Попробуйте ещё раз.")
        except ValueError:
            print("Вы ввели некорректное значение. Попробуйте ещё раз.")

def rearrange_number(num):

    n1 = num[0]
    n2 = num[1]
    n3 = num[2]
    return f"{n3}{n2}{n1}"

if __name__ == "__main__":

    three_digit_number = get_three_digit_number()
    

    rearranged_number = rearrange_number(three_digit_number)
    print(rearranged_number)
