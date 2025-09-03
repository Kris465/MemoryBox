array = [2, 4, 6, 8, 10]
A = 3


array_minus_A = [x - A for x in array]
print(f"Массив после уменьшения на {A}:", array_minus_A)

first_element = array[0]

if first_element != 0:
    array_divided = [x / first_element for x in array]
    print(f"Массив после деления на первый элемент ({first_element}):",
          array_divided)
else:
    print("Первый элемент равен нулю, деление невозможно.")
