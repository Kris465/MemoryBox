a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))


if a > b:
    print("Больше:", a)
elif b > a:
    print("Больше:", b)
else:
    print("Числа равны")


if a < b:
    print("Меньше:", a)
elif b < a:
    print("Меньше:", b)
else:
    print("Числа равны")
