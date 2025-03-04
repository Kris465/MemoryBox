
n = int(input("Введите число n: "))

position = 0

index = 1

while True:
    num = int(input("Введите целое число (для окончания введите 10000): "))

    if num == 10000:
        break

    if num > n:
        position = index
        break
    index += 1


if position > 0:
    print(f"Первое число, большее {n}, находится на позиции: {position}")
else:
    print(f"В последовательности нет чисел, больше {n}.")
