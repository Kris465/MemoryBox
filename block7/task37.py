from math import copysign


def count_sign_changes(sequence):
    if not sequence:
        return 0

    count = 0
    for i in range(1, len(sequence)):
        if copysign(1, sequence[i - 1]) != copysign(1, sequence[i]):
            count += 1
    return count


sequence = [10, -4, 12, 56, -4]
print(count_sign_changes(sequence))
