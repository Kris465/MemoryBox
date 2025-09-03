def multiplication_table_of_7():
    print("Таблица умножения на 7:")
    for i in range(1, 11):
        result = 7 * i
        print(f"7 x {i} = {result}")
    return multiplication_table_of_7


print(multiplication_table_of_7())
