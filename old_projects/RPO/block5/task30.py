sum_cubes_20_to_40 = sum(i ** 3 for i in range(20, 41))
print("Сумма кубов всех целых чисел от 20 до 40:", sum_cubes_20_to_40)

# б) Сумма квадратов всех целых чисел от a до 50
a = int(input("Введите значение a (0 <= a <= 50): "))
if 0 <= a <= 50:
    sum_squares_a_to_50 = sum(i ** 2 for i in range(a, 51))
    print(f"Сумма квадратов всех целых чисел от {a} до 50:", sum_squares_a_to_50)
else:
    print("Ошибка: значение a должно быть в диапазоне от 0 до 50.")

# в) Сумма квадратов всех целых чисел от 1 до n
n = int(input("Введите значение n (1 <= n <= 100): "))
if 1 <= n <= 100:
    sum_squares_1_to_n = sum(i ** 2 for i in range(1, n + 1))
    print(f"Сумма квадратов всех целых чисел от 1 до {n}:", sum_squares_1_to_n)
else:
    print("Ошибка: значение n должно быть в диапазоне от 1 до 100.")

# г) Сумма квадратов всех целых чисел от a до b
a = int(input("Введите значение a (a < b): "))
b = int(input("Введите значение b (a < b): "))
if a < b:
    sum_squares_a_to_b = sum(i ** 2 for i in range(a, b + 1))
    print(f"Сумма квадратов всех целых чисел от {a} до {b}:", sum_squares_a_to_b)
else:
    print("Ошибка: значение b должно быть больше значения a.")
