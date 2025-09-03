a = float(input("Введите число a (1 < a <= 1.5): "))

if not (1 < a <= 1.5):
    print("Число должно быть в диапазоне (1, 1.5].")
else:
    for n in range(1, int(1/a) + 1):
        print(1/n)