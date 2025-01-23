def main():
    while True:
        number = int(input("Введите число: "))
        base = int(input("Выберети систему счисления"))
        if base == 1:
            binary_number = bin(number)[2:]
            print(f"Число в двоичной системе счисления: {binary_number}")
        elif base == 2:
            octal_number = oct(number)[2:]
            print(f"Число в восьмеричной системе счисления: {octal_number}")
        elif base == 3:
            result = hex(number)[2:].upper()
            print(f"Число в шестнадцатеричной системе счисления:{result}")
        else:
            print("Неверный выбор системы счисления. Попробуй снова")

        flag = input("Хотите продолжить? (y/n): ")
        if flag != 'y':
            break

        f = True
        if f:
            print("True")
        else:
            print("False")


main()
