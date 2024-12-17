number = int(input("Введите трёхзначное число: "))
last_digit = number % 10
new_number = last_digit * 100 + number // 10
print(new_number)
