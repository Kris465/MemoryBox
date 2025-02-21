def print_square_sequence(n):
    for i in range(2, n + 1):
        square = i ** 2
        odd_numbers = [x for x in range(1, 2 * i, 2)]
        print(f"{i} {square} {' '.join(map(str, odd_numbers))}")


print_square_sequence(5)
