a = int(input("Введите количество чисел: "))
numbers = list(map(int, input("Введите числа через пробел: ").split()))

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

if even_numbers:
    average = sum(even_numbers) / len(even_numbers)
    print(f"Среднее арифметическое четных чисел: {average:.2f}")
else:
    print("Четных чисел нет. ")
