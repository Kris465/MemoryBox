def input_residents():
    # Ввод количества жителей в каждом доме через пробел
    data = input("Введите количество жителей в каждом доме, \
        разделённые пробелом: ")
    # Преобразуем введённые данные в список целых чисел
    residents = [int(x) for x in data.strip().split()]
    return residents


def main():
    residents = input_residents()

    # Расчет суммы жителей на нечетной стороне (дома с нечетными номерами)
    sum_odd_side = sum(residents[i] for i in range(0, len(residents), 2))
    # Расчет суммы жителей на четной стороне (дома с четными номерами)
    sum_even_side = sum(residents[i] for i in range(1, len(residents), 2))

    print(f"Общее число жителей на нечетной стороне: {sum_odd_side}")
    print(f"Общее число жителей на четной стороне: {sum_even_side}")

    if sum_odd_side > sum_even_side:
        print("На нечетной стороне проживает больше жителей.")
    elif sum_even_side > sum_odd_side:
        print("На четной стороне проживает больше жителей.")
    else:
        print("Количество жителей одинаково на обеих сторонах.")


if __name__ == "__main__":
    main()
