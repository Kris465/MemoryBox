# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму. (1 + 1/n) ** n

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def magic_list():
    number = int(input("Input yout number: "))
    ls = []
    result = 0

    for i in range(1, number + 1):
        result = (1 + 1/i) ** i
        ls.append(result)
    print(f"Your list is: {ls}") 


magic_list()