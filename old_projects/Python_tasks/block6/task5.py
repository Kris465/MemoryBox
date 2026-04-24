from itertools import takewhile


def count_equal_elements(sequence):
    return len(list(takewhile(lambda x: x == sequence[0], sequence)))


sequence = [2, 2, 2, 3, 4, 2, 2, 1, 1, 1, 5, 6, 7, 8, 9, 10, 11, 12]
print(count_equal_elements(sequence))
