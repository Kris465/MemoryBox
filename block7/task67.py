def get_pairs(n):
    pairs = []
    for i in range(n):
        pair = input(f"Введите пару чисел для {i + 1}-й пары\
            (через пробел): ").split()
        pairs.append((int(pair[0]), int(pair[1])))
    return pairs


def find_max_sum_min_product(pairs):
    max_sum = float('-inf')
    min_product = float('inf')

    for a, b in pairs:
        current_sum = a + b
        current_product = a * b

        if current_sum > max_sum:
            max_sum = current_sum

        if current_product < min_product:
            min_product = current_product

    return max_sum, min_product


n = int(input("Введите количество пар чисел: "))
pairs = get_pairs(n)
max_sum, min_product = find_max_sum_min_product(pairs)

print("Максимальная сумма значений чисел в паре:", max_sum)
print("Минимальное произведение значений чисел в паре:", min_product)
