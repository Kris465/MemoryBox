a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = int(input("Введите четвертое число: "))

result = sum(x for x in [a, b, c, d] if x % 3 == 0)

print(f"Сумма чисел, кратных трем: {result}")
