def multiplication_table():
    number = int(input("Введите число для вывода таблицы умножения: "))

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


multiplication_table()
