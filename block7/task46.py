def find_average_multiples(m, n, numbers):
    multiples = []
    for i in range(1, m+1):
        if numbers[i-1] % n == 0:
            multiples.append(numbers[i-1])
    if multiples:
        return sum(multiples) / len(multiples)
    else:
        return None


m = 12
n = 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

average = find_average_multiples(m, n, numbers)
if average is not None:
    print("Среднее арифметическое кратных чисел:", round(average, 2))
else:
    print("Нет кратных чисел.")
