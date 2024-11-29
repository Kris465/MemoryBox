num1 = int(input("Введите число num1: "))
num2 = int(input("Введите число num2: "))


def nok(num1, num2):
    minimum = num1 * num2
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return minimum // (num1 + num2)


print(nok(num1, num2))
