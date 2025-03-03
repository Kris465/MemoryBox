def count_unique_numbers(sequence):
    unique_count = 0
    previous_number = None

    for number in sequence:
        if number == 0:
            break
        if number != previous_number:
            unique_count += 1
            previous_number = number

    return unique_count


sequence = [6, 5, 4, 4, 3, 2, 2, 1, 1, 0]
result = count_unique_numbers(sequence)
print(result)
