def powers_of_two(n):
    return [2 ** i for i in range(n)]


# Ввод данных
n = int(input("Введите N (степень числа 2): "))


# Заполнение массива
result = powers_of_two(n)
print("Степени числа 2:", result)
