def find_x(n):
    if 10 <= n <= 999:

        first_digit = n // 100 if n >= 100 else n // 10


        tens = (n // 10) % 10


        x = first_digit * 100 + (tens * 2) * 10 + (n % 10)

        print(f"Найденное трехзначное число x: {x}")
    else:
        print("Число не соответствует заданным условиям.")


n = int(input("Введите число n (10 <= n <= 999): "))


find_x(n)
