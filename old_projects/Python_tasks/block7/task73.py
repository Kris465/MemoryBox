def find_two_max_min(n):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for _ in range(n):
        num = int(input("Введите целое число: "))

        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    return (max1, max2), (min1, min2)


n = int(input("Введите количество целых чисел (n >= 3): "))
if n < 3:
    print("Количество чисел должно быть не менее 3.")
else:
    (max1, max2), (min1, min2) = find_two_max_min(n)

    print("Два максимальных элемента:", max1, max2)
    print("Два минимальных элемента:", min1, min2)
