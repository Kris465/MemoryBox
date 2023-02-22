# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def conversion_of_the_number():
    number = int(input("Input your number, please: "))
    lst = []

    while number != 0:
        lst.append(number % 2)
        number = number // 2

    lst.reverse()
    print("Your number is:")
    print(*lst)

conversion_of_the_number()
