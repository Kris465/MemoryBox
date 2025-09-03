sum_a = sum(range(100, 501))
print(f"Сумма чисел от 100 до 500: {sum_a}")

a = int(input("Введите значение a (a <= 500): "))
if a > 500:
    print("Ошибка: значение a должно быть меньше или равно 500.")
else:
    sum_b = sum(range(a, 501))
    print(f"Сумма чисел от {a} до 500: {sum_b}")
    
b = int(input("Введите значение b (b >= -10): "))
if b < -10:
    print("Ошибка: значение b должно быть больше или равно -10.")
else:
    sum_c = sum(range(-10, b +1))
    print(f"Сумма чисел от -10 до {b}: {sum_c}")
    
a = int(input("Введите значение a: "))
b = int(input("Введите значение b (b >= a): "))
if b < a:
    print("Ошибка: значение b должно быть больше или равно a.")
else:
    sum_d = sum(range(a, b + 1))
    print(f"Сумма чисел от {a} до {b}: {sum_d}")
