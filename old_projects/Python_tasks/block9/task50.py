slovo_0 = input("Введите слово 1 (длинее второго): ")
slovo_1 = input("Введите слово 2: ")
result = slovo_0 + slovo_1[len(slovo_0):]
print(result)
