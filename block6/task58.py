sequence = [1, 2, ..., 15]


negative_numbers = [index + 1 for index, number
                    in enumerate(sequence) if number < 0]

if negative_numbers:
    first_negative_index = negative_numbers[0]
    print(f"Первое отрицательное\
        число находится на позиции: {first_negative_index}")
else:
    print("Отрицательных чисел нет.")
