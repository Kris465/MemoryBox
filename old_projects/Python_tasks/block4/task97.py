num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))


def find_numbers(num1, num2, num3):
    max_num = max(num1, num2, num3)
    min_num = min(num1, num2, num3)
    aver_num = (num1 + num2 + num3) - max_num - min_num

    return max_num, min_num, aver_num


max_num, min_num, aver_num = find_numbers(num1, num2, num3)

print(f"Самое наибольшее число: {max_num}")
print(f"Самое наименьшее число: {min_num}")
print(f"Среднее число: {aver_num}")
