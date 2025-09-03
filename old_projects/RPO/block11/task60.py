def input_array():
    data = input("Введите массив целых чисел, разделённых пробелом или запятой: ")
    import re
    numbers = re.split(r'[,\s]+', data.strip())
    array = [int(num) for num in numbers if num]
    return array


def main():
    array = input_array()

    sum_greater_20 = sum(x for x in array if x > 20)
    condition_a = sum_greater_20 > 100

    sum_less_50 = sum(x for x in array if x < 50)
    condition_b = (sum_less_50 % 2 == 0)

    print(f"Сумма элементов, больших 20: {sum_greater_20}")
    print(f"Условие (сумма > 100): {condition_a}")
    print(f"Сумма элементов, меньших 50: {sum_less_50}")
    print(f"Условие (сумма чётная): {condition_b}")


if __name__ == "__main__":
    main()
