from itertools import takewhile


def sum_of_consecutive_odd_numbers(numbers):
    odd_numbers = takewhile(lambda x: x % 2 != 0, numbers)
    return sum(odd_numbers)


sequence = [1, 3, 5, 7, 9, 10, 11, 13]
result = sum_of_consecutive_odd_numbers(sequence)
print(result)
