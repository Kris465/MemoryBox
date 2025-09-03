def find_kth_digit(k):
    sequence = ''.join(str(i) for i in range(50, 251))

    return sequence[k-1]


k = int(input("Введите значение k (от 1 до 252): "))
result = find_kth_digit(k)
print(f"{k}-я цифра последовательности равна {result}")
