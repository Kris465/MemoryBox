
n = int(input("Введите количество вещественных чисел: "))


if n <= 0:
    print("Количество чисел должно быть натуральным (больше 0).")
else:
    count_positive = 0
    count_negative = 0

    for i in range(n):
        number = float(input(f"Введите вещественное число {i + 1}: "))
        if number > 0:
            count_positive += 1
        elif number < 0:
            print(f"Количество положительных чисел: {count_positive}")
            print(f"Количество отрицательных чисел: {count_negative}")