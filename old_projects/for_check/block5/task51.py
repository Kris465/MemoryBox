def mixed_average(numbers, n):
    return (sum(numbers) + n) / (len(numbers) + 1)


print("среднее число 1, 2, 3, 4 и числа 4 равно:",
      mixed_average([1, 2, 3, 4], 4))
