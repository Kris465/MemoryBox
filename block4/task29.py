num = int(input("Введите трехзначное число: "))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

square_of_num = num ** 2
sum_of_cubes = (hundreds ** 3) + (tens ** 3) + (ones ** 3)

if square_of_num == sum_of_cubes:
    print("Да, квадрат числа равен сумме кубов его цифр.")
else:
    print("Нет, квадрат числа не равен сумме кубов его цифр.")
