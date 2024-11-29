number = int(input("Введите число: "))


def digits(number):
    str_number = str(number)
    return len(str_number)


print(digits(number))
