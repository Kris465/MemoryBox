def is_power_of_n(number, n):
    if number < 1:
        return False
    while number % n == 0:
        number //= n
        return number == 1


num = int(input("Введите число: "))

if is_power_of_n(num, 3):
    print(f"{num} является степенью числа 3.")
else:
    print(f"{num} не является степенью числа 3.")


if is_power_of_n(num, 5):
    print(f"{num} является степенью числа 5.")
else:
    print(f"{num} не является степенью числа 5.")
