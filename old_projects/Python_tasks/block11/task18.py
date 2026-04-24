array = [10, 20, 30, 40, 50]
B = 5

array_minus_20 = [x - 20 for x in array]
print("Массив после уменьшения на 20:", array_minus_20)

last_element = array[-1]


if last_element != 0:
    array_times_last = [x * last_element for x in array]
    print(f"Массив после ({last_element}):", array_times_last)
else:
    print("Последний элемент равен нулю, умножение не имеет смысла.")

array_plus_B = [x + B for x in array]
print(f"Массив после увеличения на {B}:", array_plus_B)
