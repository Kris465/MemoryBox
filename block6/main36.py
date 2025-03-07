# Находим первое число, кратное 9 и оканчивающееся на 7, начиная с 100
first_multiple = 100 + (9 - (100 % 9))
if first_multiple % 10 != 7:
    first_multiple += 9

# Генерируем 10 чисел
numbers = []
current = first_multiple
while len(numbers) < 10:
    if current % 10 == 7:
        numbers.append(current)
    current += 9

print("10 первых натуральных чисел, кратных 9, оканчивающихся на 7, начиная с 100:")
print(numbers)
