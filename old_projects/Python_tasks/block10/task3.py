# Способ №1
def recursive_max(x, y):
    """Рекурсивная реализация функции max"""
    if not isinstance(y, list):
        return x if x >= y else y
    elif len(y) == 1:
        return recursive_max(x, y[0])
    else:
        mid = len(y) // 2
        left_max = recursive_max(x, y[:mid])
        right_max = recursive_max(left_max, y[mid:])
        return left_max if left_max >= right_max else right_max


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
result = recursive_max(a, [b, c])
print(f"Максимальное число: {result}")

# Способ №2


def find_max_with_builtin(a, b, c):
    return max(a, b, c)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
result = find_max_with_builtin(a, b, c)
print(f"Максимальное число: {result}")
