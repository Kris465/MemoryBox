# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

def magic_list():
    number = int(input("Input yout number: "))
    ls = []
    result = 0
    sum_up = 0

    for i in range(1, number + 1):
        result = (1 + 1/i) ** i
        result = round(result, 3)
        ls.append(result)
        sum_up += result
    print(f"Your list is: {ls} \nSumma of number is: {sum_up}") 

magic_list()
