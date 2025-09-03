import math


prod_a = math.prod(range(8, 16))
print(f"Произведение чисел от 8 до 15: {prod_a}")


a = int(input("Введите значение a (1 <= a <= 20): "))
if a < 1 or a > 20:
    print("Ошибка: значение a должно быть в пределах от 1 до 20.")
else:
    prod_b = math.prod(range(a, 21))
    print(f"Произведение чисел от {a}, до 20: {prod_b}")


b = int(input("Введите значение b (1 <= b <= 20): "))
if b < 1 or b > 20:
    print("Ошибка: значение b должно быть в пределах от 1 до 20.")
else:
    prod_c = math.prod(range(1,b + 1))
    print(f"Произведение чисел от 1 до {b}: {prod_c}")
    
a = int(input("Введите значение a: "))
b = int(input("Введите значени b (b >= a): "))
if b > a:
    print("ошибка: значение b должно быть больше или равно a.")
else:
    prod_d = math.prod(range(a, b + 1))
    print(f"Произведение чисел от {a} до {b}: {prod_d}")
