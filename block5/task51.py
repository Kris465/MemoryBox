def mixed_average(numbers, n):
    return (sum(numbers) + n) / (len(numbers) + 1)


print("Среднее арифметическое чисел 1, 2, 3, 4 и числа 4 равно:",
      mixed_average([1, 2, 3, 4], 4))
