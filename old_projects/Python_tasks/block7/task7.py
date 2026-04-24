count = 0


for number in range(100, 501):
    digit_sum = sum(int(digit) for digit in str(number))
    if digit_sum == 15:
        count += 1


print("Количество чисел от 100 до 500, сумма цифр которых равна 15:", count)
