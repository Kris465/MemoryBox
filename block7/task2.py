a = int(input("Введите a:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))


if c == 0:
    print("Ошибка: c не может быть равно 0.")
elif a > b:
    print("Ошибка: a должно быть меньше или равно b.")
else:
    for number in range(a, b + 1):
        if number % c == 0:
            print(number)
