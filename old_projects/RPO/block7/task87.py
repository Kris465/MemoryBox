def count_numbers_less_than_p(b, p):
    count = 0
    for num in b:
        if num < p:
            count += 1
    return count


n = int(input("Введите количество чисел: "))
b = list(map(int, input("Введите числа через пробел: ").strip().split()))[:n]
p = int(input("Введите пороговое значение p: "))

result = count_numbers_less_than_p(b, p)
print(f"Количество чисел, меньших {p}: {result}")
