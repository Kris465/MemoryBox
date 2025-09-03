number = int(input("введите двузначное число: "))

tens = number // 10
units = number % 10

sum_digits = tens + units

a = int(input("Введите число a: "))

if sum_digits % 3 == 0:
    print(f"Сумма цифр {sum_digits} кратна 3")
else:
    print(f"Сумма цифр {sum_digits} не кратна 3")

if sum_digits % a == 0:
    print(f"Сумма цифр {sum_digits} кратна {a}")
else:
    print(f"Сумма цифр {sum_digits} не кратна {a}")
