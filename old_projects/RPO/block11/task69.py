def input_array():
    # Ввод массива целых чисел через пробел
    data = input("Введите элементы массива, разделённые пробелом: ")
    array = [int(x) for x in data.strip().split()]
    return array


def main():
    array = input_array()

    # Ввод значений a и b
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b (b > a): "))

    if b <= a:
        print("Ошибка: значение b должно быть больше a.")
        return

    # Подсчет элементов, принадлежащих промежутку [a, b]
    count = sum(1 for x in array if a <= x <= b)

    print(f"Количество элементов, принадлежащих промежутку от {a} до {b}: \
          {count}")


if __name__ == "__main__":
    main()
