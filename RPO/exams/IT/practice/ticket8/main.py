def determine_base(number_str):
    if all(c in '01' for c in number_str):
        return 2
    elif number_str.isdigit():
        return 10
    else:
        raise ValueError("Неверный формат числа. Допустимы только двоичные (0 и 1) или десятичные числа.")

def convert_number(number_str, base):
    if base == 2:
        decimal_number = int(number_str, 2)
        return decimal_number
    elif base == 10:
        binary_number = bin(int(number_str))[2:]
        return binary_number

def main():
    while True:
        number_str = input("Введите число: ")

        try:
            base = determine_base(number_str)

            if base == 2 and number_str.isdigit():
                user_choice = input(f"Число '{number_str}' может быть как двоичным, так и десятичным. "
                                    "Какую систему счисления вы имели в виду? (введите '2' для двоичной или '10' для десятичной): ")
                if user_choice == '2':
                    base = 2
                elif user_choice == '10':
                    base = 10
                else:
                    print("Неверный выбор. Попробуйте снова.")
                    continue

            result = convert_number(number_str, base)
            if base == 2:
                print(f"Число в десятичной системе счисления: {result}")
            elif base == 10:
                print(f"Число в двоичной системе счисления: {result}")

        except ValueError as e:
            print(e)

        flag = input("Хотите продолжить? (y/n): ")
        if flag.lower() != 'y':
            break


if __name__ == "__main__":
    main()
