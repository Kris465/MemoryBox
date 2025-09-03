def task_5_90(n):
    """
    Вычисляет сумму 1/1! + 1/2! + 1/3! + ... + 1/n!
    """
    if not 1 <= n <= 10:
        return "n должно быть от 1 до 10"

    result = 0
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        result += 1 / factorial
    return result


if __name__ == "__main__":
    print("Задача 5.90 (n = 5):", task_5_90(5))
