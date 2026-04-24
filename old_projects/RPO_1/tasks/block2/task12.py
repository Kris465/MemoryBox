number = int(input("Введите трехзначное число: "))
a = number % 10
b = number // 10 % 10
v = number // 100
summ = a + b + v
product = a * b * v

print(f"Число единиц в числе: {a}")
print(f"Число десятков в числе: {b}")
print(f"Сумма цифр числа: {summ}")
print(f"Произведение цифр числа: {product}")
