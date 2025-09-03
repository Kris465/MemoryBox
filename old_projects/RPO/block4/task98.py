num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
if num1 > num2 and num1 > num3:
    print("Наибольшее число: первое ", num1)
elif num2 > num3:
    print("Наибольшее число: второе ", num2)
else:
    print("Наибольшее число: третье ", num3)
if num1 < num2 and num1 < num3:
    print("Наименьшее число: первое ", num1)
elif num2 < num3:
    print("Наименьшее число: второе ", num2)
else:
    print("Наименьшее число: третье ", num3)
