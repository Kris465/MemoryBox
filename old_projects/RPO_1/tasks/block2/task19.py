import math

num = int(input("Введите четырехзначное число: "))
num = abs(num)  # если число может быть отрицательным
digits_str = str(num)
digits = [int(d) for d in digits_str]

# сумма цифр
sum_digits = sum(digits)

# произведение цифр
product_digits = math.prod(digits)

print("Сумма цифр:", sum_digits)
print("Произведение цифр:", product_digits)
