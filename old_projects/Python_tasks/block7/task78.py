
n = int(input("Введите количество чисел: "))


max_length = 0
current_length = 0

# Считываем числа
for _ in range(n):
    a = int(input("Введите число: "))

    if a % 2 == 0:
        current_length += 1
    else:

        if current_length > max_length:
            max_length = current_length
        current_length = 0


if current_length > max_length:
    max_length = current_length


print(f"Наибольшая длина отрезка четных чисел: {max_length}.")
