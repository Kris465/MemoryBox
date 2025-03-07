# Ввод последовательности чисел
numbers = []
while True:
    num = int(input("Введите число (9999 для завершения): "))
    if num == 9999:
        break
    numbers.append(num)

# Проверка на наличие пары соседних четных чисел
found = False
for i in range(len(numbers) - 1):
    if numbers[i] % 2 == 0 and numbers[i + 1] % 2 == 0:
        found = True
        print(f"Найдена пара соседних четных чисел: {numbers[i]} и {numbers[i + 1]}")
        print(f"Порядковые номера: {i + 1} и {i + 2}")
        break

if not found:
    print("В последовательности нет пары соседних четных чисел.")
