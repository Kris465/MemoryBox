def input_reverse_sequence():
    num = int(input("Введите число (нулём завершаете ввод): "))
    if num != 0:
        input_reverse_sequence()
    print(num)


input_reverse_sequence()
