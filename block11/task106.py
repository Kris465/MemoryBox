array = [2, 3, 5, 7, 4, 9, 11, 13, 2, 15]

max_length = 0
current_length = 0

for num in array:
    if num % 2 != 0:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 0

print("Наибольшая длина отрезка из нечетных чисел:", max_length)
