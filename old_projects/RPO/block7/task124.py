def count_duplicates_and_unique_numbers(sequence):
    if not sequence:
        return 0, 0

    count_duplicates = 0
    unique_numbers = set()

    current_number = sequence[0]
    current_count = 1

    for number in sequence[1:]:
        unique_numbers.add(number)
        if number == current_number:
            current_count += 1
        else:
            if current_count > 1:
                count_duplicates += current_count
            current_number = number
            current_count = 1

    if current_count > 1:
        count_duplicates += current_count

    return count_duplicates, len(unique_numbers)


sequence = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10, 10]
duplicates_count, unique_count = count_duplicates_and_unique_numbers(sequence)
print("Количество повторяющихся чисел:", duplicates_count)
print("Количество различных чисел:", unique_count)
