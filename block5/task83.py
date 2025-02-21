def power(a: float, n: int) -> float:
    result = 1.0
    for _ in range(n):
        result *= a
    return result


a = float(input("Введите число a: "))
n = int(input("Введите степень n: "))
print(f"{a}^{n} = {power(a, n)}")
