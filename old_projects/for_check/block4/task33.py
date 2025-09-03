num = int(input("Введите число: "))
last_num = (num % 10)
if last_num % 2 == 0:
    print("Оно заканчивается четным числом")
elif last_num % 2 == 1:
    print("Оно заканчивается нечетным число")
