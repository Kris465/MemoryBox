# Определение всех возможных значений A и B
values = [True, False]

# Перебираем все комбинации A и B
for A in values:
    for B in values:
        # Выражения
        result_a = (not (not A and not B)) and A
        result_b = (not (not A or not B)) or A
        result_c = (not (not A or not B)) and B

        # Вывод результатов
        print(f"A={A}, B={B} =>")
        print(f"  а) {result_a}")
        print(f"  б) {result_b}")
        print(f"  в) {result_c}")
        print('------------------------------')
