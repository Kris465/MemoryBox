def calculate_sum(expression):
    return eval(expression)


text = input("Введите выражение в формате 'd1 + d2 + ... + dn': ")
result = calculate_sum(text)
print("Результат суммы:", result)
