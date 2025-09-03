def find_multiple_of_seven(sequence):
    for i, num in enumerate(sequence):
        if num == -1:
            break
        if num % 7 == 0:
            return i + 1

    return None


test_sequence = [
    [14, 21, 5, -1],
    [4, 9, 28, -1],
    [4, 9, 10, -1],
    [21, 35, 49, -1],
]

for seq in test_sequence:
    result = find_multiple_of_seven(seq)
    print(f"Последовательность: {seq}")
    if result:
        print(f"Первое число, кратное семи, находится на позиции {result}")
    else:
        print("В последовательности нет чисел, кратных семи")
