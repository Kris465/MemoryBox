A = int(input("Введите целое число A: "))

condition_a = (A % 2 == 0) or (A % 3 == 0)

condition_b = (A % 3 != 0) and (A % 10 == 0)

print("Условие а (кратен двум или трем):", condition_a)
print("Условие б (не кратен трем и заканчивается нулем):", condition_b)
