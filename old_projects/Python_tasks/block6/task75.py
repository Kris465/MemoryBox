from random import randint


def is_valid_domino_sequence_a(numbers):

    pairs = zip(numbers, numbers[1:])
    for first, second in pairs:
        if not (first % 10 == second // 10):
            return False
        else:
            return True


numbers = [randint(0, 100) for i in range(15)]
print(is_valid_domino_sequence_a(numbers))
