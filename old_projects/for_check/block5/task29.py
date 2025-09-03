n = 1000
average_a = sum(range(1, n + 1)) / n
print("Среднее арифметическое от 1 до 1000:", average_a)

b = int(input("Введите значение b (b > 100): "))
if b > 100:
    average_b = sum(range(100, b + 1)) / (b - 100 + 1)
    print(f"Среднее арифметическое от 100 до {b}:", average_b)
else:
    print("Ошибка: b должно быть больше 100.")

a = int(input("Введите значение a (a < 200): "))
if a < 200:
    average_c = sum(range(a, 201)) / (200 - a + 1)
    print(f"Среднее арифметическое от {a} до 200:", average_c)
else:
    print("Ошибка: a должно быть меньше 200.")

a = int(input("Введите значение a: "))
b = int(input("Введите значение b (b > a): "))
if b > a:
    average_d = sum(range(a, b + 1)) / (b - a + 1)
    print(f"Среднее арифметическое от {a} до {b}:", average_d)
else:
    print("Ошибка: b должно быть больше a.")
