def input_precipitation():
    data = input("Введите количество осадков за каждый день февраля, разделённые пробелом: ")
    precipitation = [int(x) for x in data.strip().split()]
    return precipitation

def main():
    precipitation = input_precipitation()

    if len(precipitation) not in [28, 29]:
        print("Некорректное количество данных для февраля.")
        return

    sum_even_days = sum(precipitation[i] for i in range(1, len(precipitation), 2))
    sum_odd_days = sum(precipitation[i] for i in range(0, len(precipitation), 2))

    print(f"Общий осадок по четным дням: {sum_even_days}")
    print(f"Общий осадок по нечетным дням: {sum_odd_days}")

    if sum_even_days > sum_odd_days:
        print("По четным числам выпало больше осадков, чем по нечетным.")
    else:
        print("По четным числам не выпало больше осадков, чем по нечетным.")

if __name__ == "__main__":
    main()
