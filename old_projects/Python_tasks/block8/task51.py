def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


number = int(input("Введите натуральное число: "))
result = digital_root(number)
print(f"Цифровой корень числа {number}: {result}")
