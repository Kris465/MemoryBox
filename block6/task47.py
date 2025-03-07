n = int(input("Введите натуральное число: "))
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
k = int(input("Введите значение k: "))
t = int(input("Введите значение t: "))


n_str = str(n)


sum_digits = sum(int(digit) for digit in n_str)
condition_a = sum_digits < a


product_digits = 1
for digit in n_str:
    product_digits *= int(digit)
condition_b = product_digits > b


condition_c = len(n_str) == k


condition_d = int(n_str[0]) > t


print(f"Сумма цифр меньше a: {condition_a}")
print(f"Произведение цифр больше b: {condition_b}")
print(f"Число k-значное: {condition_c}")
print(f"Первая цифра больше t: {condition_d}")
