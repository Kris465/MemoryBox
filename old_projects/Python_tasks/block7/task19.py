numbers = [float(x) for x in input(
    "Введите 15 вещественных чисел через пробел: ").split()]

total_sum = 0

for i in range(0, len(numbers), 3):
    total_sum -= numbers[i]

print("Сумма отрицательных значений: ", total_sum)
