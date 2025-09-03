number = int(input("Введите трехзначное число:"))
first_digit = number // 100
new_number = (number % 100) * 10 + first_digit
print(new_number)
