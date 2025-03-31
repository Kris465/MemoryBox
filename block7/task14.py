numbers = []

for i in range(8):
    num = float(input(f"Введите {i+1}-е вещественное число: "))
    numbers.append(num)


sum_of_numbers_greater_than_1075 = 0

for number in numbers:
    if number > 10.75:
        sum_of_numbers_greater_than_1075 += number

print("Сумма чисел, больших 10.75:", sum_of_numbers_greater_than_1075)
