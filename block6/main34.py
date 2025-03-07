# Находим первое число, кратное 19, начиная с 100
first_multiple = 100 + (19 - (100 % 19))

# Генерируем 15 чисел, кратных 19
multiples = list(range(first_multiple, first_multiple + 19 * 15, 19))

print("15 первых натуральных чисел, кратных 19, начиная с 100:")
print(multiples)
