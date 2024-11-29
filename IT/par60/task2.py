num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))
num3 = int(input("Введите число 3: "))


def minimum_maximum(num1, num2, num3):
    spisok = [num1, num2, num3]
    maximum = max(spisok)
    minimum = min(spisok)
    return maximum, minimum


print(minimum_maximum(num1, num2, num3))
