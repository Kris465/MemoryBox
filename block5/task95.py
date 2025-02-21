def task_5_95(num, n):
    str_num = str(num)
    if len(str_num) < n:
        return "Число меньше чем n цифр"

    return sum(int(digit) for digit in str_num[-n:])


print("Задача 5.95 (123456, 3):", task_5_95(123456, 3))
