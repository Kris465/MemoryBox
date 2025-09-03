from itertools import takewhile


def count_leading_negatives(sequence):
    return len(list(takewhile(lambda x: x < 0, sequence)))


sequence = [-2, -1, -3, 0, 1, -4, 5]
print(count_leading_negatives(sequence))
