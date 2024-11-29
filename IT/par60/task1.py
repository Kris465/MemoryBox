num1 = int(input("Введите число num1: "))
num2 = int(input("Введите число num2: "))
num3 = int(input("Введите число num3: "))


def maximum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3


print(maximum(num1, num2, num3))
