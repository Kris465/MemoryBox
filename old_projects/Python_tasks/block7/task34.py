m = int(input("Введите количество целых чисел (m): "))

if m <= 0:
    print("Количество чисел должно быть натуральным (больше 0).")
else:

    count_div_3 = 0
    count_div_7 = 0

    for i in range(m):
        number = int(input(f"Введите целое число {i + 1}: "))

        if number % 3 == 0:
            count_div_3 += 1
        if number % 7 == 0:
            count_div_7 += 1

    print(f"Количество чисел, кратных 3: {count_div_3}")
    print(f"Количество чисел, кратных 7: {count_div_7}")
