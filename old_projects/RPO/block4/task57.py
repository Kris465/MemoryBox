def digit(number, digit):
    return str(digit) in str(number)


number = int(input("Введите трёхзначное число: "))
n = int(input("Введите цифру для проверки: "))

if digit(number, 6):
    print("Цифра 6 входит в число")
else:
    print("Цифра 6 не входит в число")

if digit(number, n):
    print(f"Цифра {n} входит в число")
else:
    print(f"Цифра {n} не входит в число")
