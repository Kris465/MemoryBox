def find_first_odd(numbers):
    """Находит номер первого нечетного элемента (счёт с 1)."""
    for i, num in enumerate(numbers):
        if num % 2 != 0:
            return i + 1
    return "Нечетных элементов в массиве нет."


def find_first_multiple_13(numbers):
    """Находит номер первого элемента, кратного 13 (счёт с 1)."""
    for i, num in enumerate(numbers):
        if num % 13 == 0 and num != 0:
            return i + 1
    return "Элементов, кратных числу 13, в массиве нет."


arr = [2, 4, 6, 7, 13, 26, 39]


print("а) Номер первого нечетного элемента:", find_first_odd(arr))
print("б) Номер первого элемента, кратного 13:", find_first_multiple_13(arr))
