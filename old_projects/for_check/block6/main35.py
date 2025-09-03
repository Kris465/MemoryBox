# Находим первое число, кратное 13 или 17, начиная с 500
first_multiple = 500
while first_multiple % 13 != 0 and first_multiple % 17 != 0:
    first_multiple += 1

# Генерируем 20 чисел, кратных 13 или 17
multiples = []
current = first_multiple
while len(multiples) < 20:
    if current % 13 == 0 or current % 17 == 0:
        multiples.append(current)
    current += 1

print("20 первых натуральных чисел, кратных 13 или 17, начиная с 500:")
print(multiples)
