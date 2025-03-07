def print_numbers_not_less_than_a(a):
    k = 2
    while True:
        number = 1 + 1 / k
        if number < a:
            break
        print(number)
        k += 1


a = float(input("Введите число a (1 < a <= 1.5): "))


if a <= 1 or a > 1.5:
    print("Ошибка: число a должно быть в диапазоне (1, 1.5].")
else:
    print("Числа, которые не меньше", a, ":")
    print_numbers_not_less_than_a(a)
