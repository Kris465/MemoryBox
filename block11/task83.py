array = list(map(float, input("Введите числа через пробел: ").split()))
m = float(input("Введите число m: "))
elements_less_than_m = [x for x in array if x < m]
if len(elements_less_than_m) == 0:
    print("Нет элементов меньше", m)
else:
    average = sum(elements_less_than_m) / len(elements_less_than_m)
    print("Среднее арифметическое элементов, меньших", m, ":", average)
