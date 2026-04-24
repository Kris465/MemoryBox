array = list(map(float, input("Введите числа через пробел: ").split()))

elements_greater_than_10 = [x for x in array if x > 10]

if len(elements_greater_than_10) == 0:
    print("Нет элементов больше 10.")
else:
    average = sum(elements_greater_than_10) / len(elements_greater_than_10)
    print("Среднее арифметическое элементов, больших 10:", average)