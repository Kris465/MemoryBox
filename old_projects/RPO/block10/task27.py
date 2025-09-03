def gcd(a, b):
    """Вычисляет НОД двух чисел с помощью алгоритма Евклида."""
    while b != 0:
        a, b = b, a % b
    return a


def main():
    n = int(input("Введите количество чисел: "))
    numbers = []
    for _ in range(n):
        num = int(input("Введите число: "))
        numbers.append(num)
    current_gcd = numbers[0]
    for num in numbers[1:]:
        current_gcd = gcd(current_gcd, num)
    print(f"Наибольший общий делитель: {current_gcd}")


if __name__ == "__main__":
    main()
