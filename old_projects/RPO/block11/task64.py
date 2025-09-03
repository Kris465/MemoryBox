def input_array():
    data = input("Введите элементы массива, разделённые пробелом: ")
    array = [int(x) for x in data.strip().split()]
    return array


def main():
    array = input_array()
    if not array:
        print("Массив пустой.")
        return
    last_element = array[-1]
    count_diff_last = sum(1 for x in array if x != last_element)
    count_multiples_a = sum(1 for x in array if a != 0 and x % last_element == 0)

    print(f"Количество элементов, отличных от последнего: {count_diff_last}")
    print(f"Количество элементов, кратных {last_element}: {count_multiples_a}")


if __name__== "__main__":
    main()
