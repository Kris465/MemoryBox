def find_extremes():
    n = int(input("Введите количество чисел: "))
    numbers = []

    print(f"Введите {n} целых числа через пробел:")
    for _ in range(n):
        number = int(input())
        numbers.append(number)

    max_value = max(numbers)
    min_value = min(numbers)

    max_index = numbers.index(max_value)
    min_index = numbers.index(min_value)

    if max_index < min_index:
        print("Максимальное число встречается раньше.")
    elif min_index < max_index:
        print("Минимальное число встречается раньше.")
    else:
        print("Максимальное\
            и минимальное числа встречаются в один и тот же момент.")


find_extremes()
