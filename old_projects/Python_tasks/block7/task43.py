def average_above_10(numbers):

    filtered_numbers = [x for x in numbers if x > 10]

    return sum(filtered_numbers) / len(filtered_numbers)


numbers = [8.5, 12.3, 9.9, 15.0, 10.1, 7.8, 11.2, 13.4, 14.5]
result = average_above_10(numbers)
print(f"Среднее арифметическое чисел, больших 10: {result}")
