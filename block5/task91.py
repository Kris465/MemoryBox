def task_5_91(n, x):
    """
    Вычисляет сумму 1 + x¹/1! + x²/2! + x³/3! + ... + xⁿ/n!
    """
    if not 1 <= n <= 10:
        return "n должно быть от 1 до 10"

    result = 1
    factorial = 1
    x_power = 1
    for i in range(1, n + 1):
        x_power *= x
        factorial *= i
        result += x_power / factorial
    return result


print("Задача 5.91 (n=5, x=2):", task_5_91(5, 2))
