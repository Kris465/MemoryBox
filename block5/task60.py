def find_number_ending_with_seven(sequence):

    for i, num in enumerate(sequence):
        if str(num)[-1] == '7':
            return i + 1
        return None

    numbers = [42, 117, 23, 67, 89, 157, 234]
    result = find_number_ending_with_seven(numbers)

    if result:
        print(f"Первое число, оканчивающееся\
               на 7,находится на позиции{result}")
    else:
        print("В последовательности нет чисел, оканчивающихся на 7")
