def find_numbers_with_digit_sum(n):
    results = []
    for num in range(100, 1000):
        digits = list(map(int, str(num)))
        if sum(digits) == n:
            results.append(num)
    return results


n = int(input("Введите n (n <= 27): "))
if n > 27:
    print("Ошибка: n должно быть <= 27")
else:
    numbers = find_numbers_with_digit_sum(n)
    print(f"Трехзначные числа с суммой цифр {n}:", numbers)
