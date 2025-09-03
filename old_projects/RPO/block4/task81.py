a = int(input("Введите первое число: "))
b = int(input("Введите второе число:"))
c = int(input("Введите третье число:"))
d = int(input("Введите четвёртое число:"))


negative_count = (a < 0) + (b < 0) + (c < 0) + (d < 0)

print(f"Колличество отрицательных чисел: {negative_count}")
