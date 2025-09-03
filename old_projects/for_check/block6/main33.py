# Способ а) без цикла с условием
multiples_a = list(range(13, 100, 13))
print("Способ а) без цикла с условием:")
print(multiples_a)

# Способ б) с циклом с условием
multiples_b = []
i = 13
while i < 100:
    multiples_b.append(i)
    i += 13
print("\nСпособ б) с циклом с условием:")
print(multiples_b)

# Проверка, что оба способа дают одинаковый результат
print("\nПроверка равенства результатов:")
print(multiples_a == multiples_b)
