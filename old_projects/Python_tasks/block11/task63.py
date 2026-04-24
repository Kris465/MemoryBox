def input_array():
    data = input("Введите элементы массива, разделённые пробелом: ")
    array = [int(x) for x in data.strip().split()]
    return array


def count_non_negative(array):
    count = sum(1 for x in array if x >= 0)
    return count


def main():
    array = input_array()
    result = count_non_negative(array)
    print(f"Количество неотрицательных элементов: {result}")


if __name__ == "__main__":
    main()
