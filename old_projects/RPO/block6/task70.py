numbers = []

print("Введите вещественные числа (вводите 10000 для завершения ввода):")

while True:
    num = float(input())
    if num == 10000:
        break
    numbers.append(num)


is_sorted = True
first_violation_index = -1

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        first_violation_index = i + 1
        break

# Вывод результата
if is_sorted:
    print("Последовательность упорядочена по возрастанию.")
else:
    print(f"Последовательность не упорядочена. Первое нарушающее число на \
        позиции {first_violation_index} (значение: \
            {numbers[first_violation_index]}).")
