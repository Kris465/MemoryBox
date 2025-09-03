numbers = []
for i in range(10):
    number = int(input(f"Введите {i+1}-е целое число: "))
    numbers.append(number)

positive_count = sum(1 for num in numbers if num > 0)


if positive_count <= 5:
    print("Количество положительных чисел не превышает 5.")
else:
    print("Количество положительных чисел превышает 5.")
