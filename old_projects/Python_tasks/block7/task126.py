
numbers = input("Введите 30 чисел, разделенных пробелами: ").split()


numbers = list(map(int, numbers))


if len(numbers) != 30:
    print("Ошибка: необходимо ввести ровно 30 чисел.")
else:
    unique_numbers = set(numbers)

print("Количество различных чисел в последовательности:", len(unique_numbers))
