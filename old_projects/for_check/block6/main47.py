def check_conditions(n, a, b, k, m):
    # Преобразуем число в строку для работы с его цифрами
    n_str = str(n)
    
    # a) Верно ли, что сумма его цифр меньше a?
    sum_of_digits = sum(int(digit) for digit in n_str)
    condition_a = sum_of_digits < a

    # b) Верно ли, что произведение его цифр больше b? 
    product_of_digits = 1
    for digit in n_str:
        product_of_digits *= int(digit)
    condition_b = product_of_digits > b

    # в) Верно ли, что это число k-значное? 
    condition_v = len(n_str) == k

    # г) Верно ли, что его первая цифра превышает m?
    first_digit = int(n_str[0])
    condition_g = first_digit > m

    return condition_a, condition_b, condition_v, condition_g

# Пример использования:
n = 12345  # натуральное число
a = 20
b = 100
k = 5
m = 1

results = check_conditions(n, a, b, k, m)
print(f"Сумма цифр меньше {a}: {results[0]}")
print(f"Произведение цифр больше {b}: {results[1]}")
print(f"Число {n} является {k}-значным: {results[2]}")
print(f"Первая цифра больше {m}: {results[3]}")
