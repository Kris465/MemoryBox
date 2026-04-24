def convert_to_base(n, base):
    digits = "0123456789ABCDEF"
    if n < base:
        print(digits[n], end='')
    else:
        convert_to_base(n // base, base)
        print(digits[n % base], end='')


if __name__ == "__main__":
    X = int(input("Введите число: "))
    N = int(input("Введите основание системы счисления (2 ≤ N ≤ 16): "))
    if not (2 <= N <= 16):
        print("Ошибка: Основание должно быть от 2 до 16.")
    else:
        print(f"Число {X} в системе счисления с основанием {N}: ", end='')
        convert_to_base(X, N)
        print()  # Новая строка для красоты
