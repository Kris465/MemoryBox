a2 = int(input("Введите число десятков первого числа (a2): "))
a1 = int(input("Введите число единиц первого числа (a1): "))
b1 = int(input("Введите число единиц второго числа (b1): "))
b2 = int(input("Введите число десятков второго числа (b2): "))


first_number = a2 * 10 + a1
second_number = b2 * 10 + b1


result = first_number + second_number


result_tens = result // 10
result_units = result % 10


print("Сумма двух чисел:", result)
print("Десятки результата:", result_tens)
print("Единицы результата:", result_units)
