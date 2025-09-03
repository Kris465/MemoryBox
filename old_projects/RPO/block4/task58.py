number = int(input("Введите трехзначное число: "))


def check_digits(number):
    str_number = str(number)

    contains_4_7 = "4" in str_number or "7" in str_number
    contains_3_6_9 = "3" in str_number or "6" \
        in str_number or '9' in str_number

    return contains_4_7, contains_3_6_9


contains_4_7, contains_3_6_9 = check_digits(number)


if contains_4_7:
    print("В числе есть 4 или 7")
else:
    print('В числе нету 4 или 7')


if contains_3_6_9:
    print("В числе есть 3 или 6 или 9")
else:
    print("В числе нету 3 6 или 9")
