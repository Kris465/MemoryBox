def main():

    n = int(input("Введите количество вещественных чисел n: "))

    p = float(input("Введите значение p: "))

    total_sum = 0

    for _ in range(n):

        x = float(input(f"Введите вещественное число № {_ + 1}: "))

        if x > p:
            total_sum += x

    print(f"Сумма вещественных чисел, больших {p}, равна {total_sum}")


if __name__ == "__main__":
    main()
