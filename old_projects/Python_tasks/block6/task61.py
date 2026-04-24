position = 0
index = 1
while True:
    num = int(input("Введите целое число (для окончания введите -1): "))
    if num == -1:
        break
    if num % 7 == 0:
        position = index
        break
    index += 1
if position > 0:
    print(f"Первое число, кратное семи, находится на позиции: {position}")
else:
    print("В последовательности нет чисел, кратных семи.")
