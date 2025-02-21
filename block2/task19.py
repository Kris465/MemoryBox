num = int(input("Введите четырёхзначное число: "))

# a)
one_num = num % 10
two_num = (num // 10) % 10
three_num = (num // 100) % 10
four_num = (num // 1000) % 10
sum_num = one_num + two_num + three_num + four_num
print(f"Сумма четырёхзначного числа: {sum_num}")

# б)
proizv_num = one_num * two_num * three_num * four_num
print(f"Произведение четырёхзначного числа: {proizv_num}")
