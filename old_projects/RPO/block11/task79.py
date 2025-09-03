array = list(map(float, input(
    "Введите вещественные числа через пробел: ").split()))

positive_count = sum(1 for x in array if x > 0)
if positive_count <= 5:
    print("Верно: количество положительных элементов не превышает 5.")
else:
    print("Неверно: количество положительных элементов превышает 5.")

count_not_more_50_55 = sum(1 for x in array if x <= 50.55)
if count_not_more_50_55 % 4 == 0:
    print("Верно: количество элементов, не больше 50.55, кратно 4.")
else:
    print("Неверно: количество элементов, не больше 50.55, не кратно 4.")
