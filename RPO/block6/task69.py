def check_order(sequence):
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            return i + 1
    return 0


a = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0,
     14.0, 15.0]
result = check_order(a)

if result == 0:
    print("Последовательность упорядочена по возрастанию.")
else:
    print("Упорядочена" if result == 0 else f"На {result}-м месте ошибка")
