n = int(input("Введите натуральное число (p > 99): "))


if n > 99:

    str_n = str(n)

    for i in range(len(str_n)):
        if i == 2:
            third_digit = str_n[i]
            break

    print(f"Третья цифра числа: {third_digit}")
else:
    print("Ошибка: число должно быть больше 99.")
