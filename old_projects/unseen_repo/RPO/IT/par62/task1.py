def arithmetic_progression(first_term, difference, n):
    return [first_term + i * difference for i in range(n)]


# Ввод данных
first_term = int(input("Введите первый элемент арифметической прогрессии: "))
difference = int(input("Введите разность арифметической прогрессии: "))
n = int(input("Введите количество элементов: "))


# Заполнение массива
result = arithmetic_progression(first_term, difference, n)
print("Арифметическая прогрессия:", result)
