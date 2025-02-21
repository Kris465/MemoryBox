import math


def task_5_93a(n):
    """
    Вычисляет сумму 1/sin1 + 1/(sin1 + sin2) + ... + 1/(sin1 + ... + sinn)
    """
    result = 0
    sum_sin = 0
    for i in range(1, n + 1):
        sum_sin += math.sin(i)
        result += 1 / sum_sin
    return result


def task_5_93b(n):
    """
    Вычисляет √2 + √2 + ... + √2 (n слагаемых)
    """
    result = 0
    for _ in range(n):
        result = math.sqrt(2 + result)
    return result


def task_5_93c(n):
    """
    Вычисляет (cos1/sin1) + (cos1+cos2)/(sin1+sin2)
    + ... + (cos1+...+cosn)/(sin1+...+sin2n)
    """
    sum_cos = 0
    sum_sin = 0
    result = 0
    for i in range(1, n + 1):
        sum_cos += math.cos(i)
        sum_sin += math.sin(i) + math.sin(2*i)
        result += sum_cos / sum_sin
    return result


def task_5_93d(n):
    """
    Вычисляет √3 + √6 + ... + √(3(n-1)) + √3n
    """
    return sum(math.sqrt(3*i) for i in range(1, n + 1))


print("Задача 5.93a (n=3):", task_5_93a(3))
print("Задача 5.93b (n=3):", task_5_93b(3))
print("Задача 5.93c (n=3):", task_5_93c(3))
print("Задача 5.93d (n=3):", task_5_93d(3))
