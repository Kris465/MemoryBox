# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def conversion_of_the_number():
    number = int(input("Input your number, please: "))
    lst = []

    while number != 0:
        lst.append(number % 2)
        number = number // 2

    lst.reverse()
    print(f"Your number is: {lst}")

conversion_of_the_number()