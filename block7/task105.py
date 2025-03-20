n = int(input("Введите количество чисел n: "))

Ci = []

for i in range(n):
    Ci.append(int(input(f"Введите число C{i+1}: ")))

count_less_than_20 = sum(1 for x in Ci if x < 20)

if count_less_than_20 == 5:
    print("Количество чисел, меньших 20, равно пяти.")
else:
    print("Количество чисел, меньших 20, не равно пяти.")
