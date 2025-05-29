array = list(map(float, input("Введите числа через пробел: ").split()))

positive_numbers = [x for x in array if x > 0]
negative_numbers = [x for x in array if x < 0]

# average1 = sum(positive_numbers) / len(positive_numbers)

average2 = sum(negative_numbers) / len(negative_numbers)

# print("Среднее арифметическое положительных элементов", average1)
print("Среднее арифметическое отрицательных элементов", average2)
