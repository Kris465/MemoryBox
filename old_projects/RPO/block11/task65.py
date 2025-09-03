def input_precipitation():
    # Ввод количества осадков за каждый день февраля через пробел
    data = input("Введите количество осадков за каждый день февраля, \
                 разделённые пробелом: ")
    # Преобразуем введённые данные в список целых чисел
    precipitation = [int(x) for x in data.strip().split()]
    return precipitation


def main():
    precipitation = input_precipitation()

    # Подсчет дней без осадков (осадки равны нулю)
    days_without_precipitation = sum(1 for x in precipitation if x == 0)

    print(f"Количество дней без осадков: {days_without_precipitation}")


if __name__ == "__main__":
    main()
