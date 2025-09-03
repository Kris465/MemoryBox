def solve(sequence):

    count_same_groups = 0
    distinct_numbers = set()

    n = len(sequence)

    current_number = sequence[0]
    current_count = 1
    distinct_numbers.add(current_number)

    for i in range(1, n):
        if sequence[i] == current_number:
            current_count += 1
        else:
            if current_count > 1:
                count_same_groups += 1
            current_number = sequence[i]
            current_count = 1
        distinct_numbers.add(sequence[i])

    if current_count > 1:
        count_same_groups += 1

    return count_same_groups, len(distinct_numbers)


sequence = [1.5, 2.0, 2.0, 3.5, 5.0, 5.0, 5.0, 1000.0]
same_groups, distinct_count = solve(sequence)
print("Количество групп одинаковых чисел:", same_groups)
print("Количество различных чисел:", distinct_count)
