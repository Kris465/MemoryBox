def calculate_n(x):
    last_digit = x % 10
    quotient = x // 10
    n = int(str(last_digit) + str(quotient))
    return n


def find_x(n):
    last_digit_n = n % 10
    quotient_n = n // 10
    x = last_digit_n * 10 + quotient_n
    return x


n = int(input("Введите число n (10 <= n <= 999, десятков не равно нулю): "))
if 10 <= n <= 999 and (n // 10) % 10 != 0:
   x = find_x(n)
   print(f"Найденное число x: {x}")
else:
    print("Некорректное число n. Убедитесь, что 10 <= n <= 999 и десяток не равно нулю.")
