a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = 1 if a % b == 0 or b % a == 0 else 0
print(result)
