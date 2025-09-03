from itertools import takewhile


def count_negative_at_start(numbers):
    negative_count = len(list(takewhile(lambda x: x < 0, numbers)))
    return negative_count


sequence = [-1.5, -2.8, -3.1, 4.0, 5.6, -7.2, 8.9]
result = count_negative_at_start(sequence)
print(result)  