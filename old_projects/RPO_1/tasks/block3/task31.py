N = int(input("Введите целое число N: "))

condition_a = (N % 5 == 0) or (N % 7 == 0)

condition_b = (N % 4 == 0) and (N % 10 != 0)


print("Условие а (кратно пяти или семи):", condition_a)
print("Условие б (кратно четырем и не заканчивается нулем):", condition_b)