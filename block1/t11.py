numbers = [i for i in input("Введите четыре числа через пробелы").split()]
print(*[f"{i}\n" for i in numbers])

numbers = input("Введите число из четырех цифр: ")
for i in numbers:
    k = int(i)
    print(k, type(k))

numbers = [i for i in input("Введите четыре числа через пробелы").split()]
for i in numbers:
    print(i)
