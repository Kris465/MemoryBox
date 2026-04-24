leg1 = int(input("Введите катет 1: "))
leg2 = int(input("Введите катет 2: "))
hypotenuse = round(((leg1 ** 2) + (leg2 ** 2)) ** 0.5, 2)
p = hypotenuse + leg1 + leg2
print("Периметр = ", p)
